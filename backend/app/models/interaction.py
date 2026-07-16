from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_id = Column(Integer, ForeignKey("hcps.id"), nullable=False)

    visit_date = Column(Date)

    visit_type = Column(String(50))

    notes = Column(String)

    summary = Column(String)

    next_action = Column(String)      # NEW

    follow_up = Column(String)        # NEW

    follow_up_date = Column(Date)

    created_at = Column(DateTime, default=datetime.utcnow)

    hcp = relationship("HCP", back_populates="interactions")




# import sqlite3 as sql