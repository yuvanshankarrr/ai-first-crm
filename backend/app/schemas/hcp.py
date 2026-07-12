from pydantic import BaseModel, EmailStr
from typing import Optional


class HCPCreate(BaseModel):
    name: str
    specialization: Optional[str] = None
    hospital: Optional[str] = None
    city: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class HCPResponse(HCPCreate):
    id: int

    model_config = {
        "from_attributes": True
    }



