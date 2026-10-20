import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

logger = logging.getLogger("travel_planner.database")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://traveluser:travelpassword@localhost:5432/travel_planner"
)

# Declarative Base
Base = declarative_base()


def build_engine():
    """
    Connects to PostgreSQL if running (e.g. via Docker Compose).
    If PostgreSQL is offline or Docker is not running, seamlessly falls back
    to local SQLite database so the app is immediately, fully functional with zero lag.
    """
    try:
        pg_engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
            connect_args={"connect_timeout": 1}
        )
        with pg_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Successfully connected to PostgreSQL database.")
        return pg_engine, "PostgreSQL (Docker/Local)"
    except Exception as e:
        logger.info(f"PostgreSQL not detected on port 5432 ({e}). Using persistent local SQLite database.")
        sqlite_engine = create_engine(
            "sqlite:///./travel_planner.db",
            connect_args={"check_same_thread": False}
        )
        return sqlite_engine, "Local SQLite Database (Auto-Active)"


engine, DB_BACKEND_NAME = build_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """FastAPI dependency to yield a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initializes tables in the active database."""
    try:
        import models  # noqa: F401
        Base.metadata.create_all(bind=engine)
        logger.info(f"Database tables verified/created on {DB_BACKEND_NAME}.")
        return True
    except Exception as e:
        logger.warning(f"Could not initialize tables: {e}")
        return False


def check_db_connection() -> dict:
    """Checks whether the database connection is alive."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "connected", "database": DB_BACKEND_NAME}
    except Exception as e:
        return {"status": "disconnected", "error": str(e)}
