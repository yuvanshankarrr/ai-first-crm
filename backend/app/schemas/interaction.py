from datetime import date
from typing import Optional

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

    model_config = {
        "from_attributes": True
    }