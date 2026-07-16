from sqlalchemy.orm import Session

from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate


def create_hcp(db: Session, hcp: HCPCreate):
    db_hcp = HCP(**hcp.model_dump())

    db.add(db_hcp)
    db.commit()
    db.refresh(db_hcp)

    return db_hcp


def get_all_hcps(db: Session):
    return db.query(HCP).all()


def get_hcp_by_id(db, hcp_id: int):
    return db.query(HCP).filter(HCP.id == hcp_id).first()