from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

app = FastAPI()


class RegisterUser(BaseModel):
    email: str
    password: str
    date_of_birth: str


@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }


@app.post("/register")
def register(user: RegisterUser):
    try:
        response = supabase.table("users").insert({
            "email": user.email,
            "password_hash": user.password,
            "date_of_birth": user.date_of_birth
        }).execute()

        return {
            "message": "User Created",
            "data": response.data
        }

    except Exception as e:
        return {
            "error": str(e)
        }