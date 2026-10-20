from typing import List, Optional, Any
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, Field


# ==========================================
# AUTH SCHEMAS
# ==========================================

class RegisterUser(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, description="User password (min 6 chars)")
    date_of_birth: date

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "traveler@example.com",
                "password": "secretpassword123",
                "date_of_birth": "1998-05-15"
            }
        }
    }


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordUser(BaseModel):
    email: EmailStr
    date_of_birth: date
    new_password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    id: str
    email: str
    date_of_birth: Optional[date] = None
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


# ==========================================
# PREFERENCES SCHEMAS
# ==========================================

class PreferenceData(BaseModel):
    user_id: str
    destination: str
    traveler_type: str = "Solo Explorer"
    budget_tier: str = "Balanced"
    trip_mood: str = "Hidden Gems"
    dietary_profile: str = "Foodie"
    accessibility_needs: Optional[str] = "None"


class PreferenceResponse(BaseModel):
    id: str
    user_id: str
    destination: str
    traveler_type: str
    budget_tier: str
    trip_mood: str
    dietary_profile: str
    accessibility_needs: Optional[str] = None
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


# ==========================================
# ITINERARY SCHEMAS
# ==========================================

class Activity(BaseModel):
    activity_name: str
    time_slot: str
    ticket_requirement: str
    estimated_price: str
    insider_booking_tip: str


class DayItinerary(BaseModel):
    day: int
    title: Optional[str] = None
    activities: List[Activity]


class ItineraryRequest(BaseModel):
    user_id: str
    destination: str
    duration_days: int = Field(default=3, ge=1, le=30)
    traveler_type: Optional[str] = "Solo Explorer"
    budget_tier: Optional[str] = "Balanced"
    trip_mood: Optional[str] = "Hidden Gems"
    dietary_profile: Optional[str] = "Foodie"
    accessibility_needs: Optional[str] = "None"
    api_key: Optional[str] = None
    ai_provider: Optional[str] = "gemini"  # "gemini" or "openai"



class ItineraryRecordResponse(BaseModel):
    id: str
    user_id: str
    destination: str
    duration_days: int
    trip_data: List[Any]
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}
