from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate
from app.services.ai_service import generate_summary



def create_interaction(db: Session, interaction: InteractionCreate):
    summary = generate_summary(interaction.notes)
    db_interaction = Interaction(
        **interaction.model_dump(),
        summary=summary
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_all_interactions(db: Session):
    return db.query(Interaction).all()