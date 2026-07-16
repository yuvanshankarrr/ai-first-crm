from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.hcp import HCPCreate, HCPResponse
from app.services.hcp_service import create_hcp, get_all_hcps

from fastapi import HTTPException

from app.services.hcp_service import (
    create_hcp,
    get_all_hcps,
    get_hcp_by_id,
)

router = APIRouter(prefix="/hcps", tags=["HCP"])


@router.post("/", response_model=HCPResponse)
def add_hcp(hcp: HCPCreate, db: Session = Depends(get_db)):
    return create_hcp(db, hcp)


@router.get("/", response_model=list[HCPResponse])
def list_hcps(db: Session = Depends(get_db)):
    return get_all_hcps(db)


@router.get("/{hcp_id}")
def get_hcp(hcp_id: int, db: Session = Depends(get_db)):

    hcp = get_hcp_by_id(db, hcp_id)

    if not hcp:
        raise HTTPException(
            status_code=404,
            detail="HCP not found"
        )

    return hcp