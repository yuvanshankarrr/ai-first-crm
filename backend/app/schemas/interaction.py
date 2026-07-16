from datetime import date
from typing import Optional
from app.schemas.hcp import HCPResponse
from pydantic import BaseModel


class InteractionCreate(BaseModel):
    hcp_id: int
    visit_date: date
    visit_type: str
    notes: str
    follow_up_date: Optional[date] = None


class InteractionResponse(InteractionCreate):
    id: int
    summary: Optional[str] = None
    next_action: Optional[str] = None
    follow_up: Optional[str] = None
    hcp: HCPResponse

    model_config = {
        "from_attributes": True
    }