from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import BloodRequest, User
from app.schemas.schemas import (
    BloodRequestCreate,
    BloodRequestResponse,
    BloodRequestUpdate,
)

router = APIRouter(prefix="/blood-requests", tags=["blood-requests"])


@router.post(
    "/", response_model=BloodRequestResponse, status_code=status.HTTP_201_CREATED
)
def create_blood_request(
    request: BloodRequestCreate, user_id: int = 1, db: Session = Depends(get_db)
):
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    db_request = BloodRequest(**request.dict(), created_by=user_id)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


@router.get("/{request_id}", response_model=BloodRequestResponse)
def get_blood_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(BloodRequest).filter(BloodRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blood request not found"
        )
    return db_request


@router.get("/", response_model=list[BloodRequestResponse])
def list_blood_requests(
    status_filter: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(BloodRequest)
    if status_filter:
        query = query.filter(BloodRequest.status == status_filter)
    requests = query.offset(skip).limit(limit).all()
    return requests


@router.put("/{request_id}", response_model=BloodRequestResponse)
def update_blood_request(
    request_id: int, update: BloodRequestUpdate, db: Session = Depends(get_db)
):
    db_request = db.query(BloodRequest).filter(BloodRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blood request not found"
        )

    update_data = update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_request, field, value)

    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


@router.delete("/{request_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blood_request(request_id: int, db: Session = Depends(get_db)):
    db_request = db.query(BloodRequest).filter(BloodRequest.id == request_id).first()
    if not db_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blood request not found"
        )
    db.delete(db_request)
    db.commit()
