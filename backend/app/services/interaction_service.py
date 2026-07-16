from sqlalchemy.orm import Session

from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate
from app.services.ai_service import analyze_interaction



def create_interaction(db: Session, interaction: InteractionCreate):
    ai_result = analyze_interaction(interaction.notes)

    db_interaction = Interaction(
        **interaction.model_dump(),
        summary=ai_result["summary"],
        next_action=ai_result["next_action"],
        follow_up=ai_result["follow_up"],
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_all_interactions(db: Session):
    # return db.query(Interaction).all()
    from sqlalchemy.orm import joinedload

    return (
        db.query(Interaction)
            .options(joinedload(Interaction.hcp))
            .all()
)