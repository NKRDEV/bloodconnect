from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.models import User,PasswordResetToken
from app.core.security import hash_password,create_access_token,verify
from app.core.email import send_reset_email
import secrets
from datetime import datetime, timedelta
from app.schemas.schemas import UserCreate, UserResponse, UserUpdate,LoginRequest, Token,ForgotPasswordRequest, ResetPasswordRequest

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    hashed_password = hash_password(user.password) 
    user.password = hashed_password   

    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


@router.get("/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    db.delete(db_user)
    db.commit()



@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token = create_access_token({"sub": str(user.email)})
    return {"access_token": access_token}

@router.post("/logout")
def logout():
    return {"message": "Logout successful. Delete token on client side."}

@router.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        return {"message": "If the email exists, a reset link was sent"}

    token = secrets.token_urlsafe(32)

    reset = PasswordResetToken(
        users_id=user.id,
        token=token,
        expires_at=datetime.utcnow() + timedelta(minutes=15),
    )

    db.add(reset)
    db.commit()
    await send_reset_email(user.email, token)
    return {"message": "If the email exists, a reset link was sent"}

@router.post("/reset-password")
def reset_password(data: ResetPasswordRequest, db: Session = Depends(get_db)):
    reset = (
        db.query(PasswordResetToken)
        .filter(
            PasswordResetToken.token == data.token,
            PasswordResetToken.used == False,
            PasswordResetToken.expires_at > datetime.utcnow(),
        )
        .first()
    )

    if not reset:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = db.query(User).filter(User.id == reset.users_id).first()

    user.password = hash_password(data.new_password)
    reset.used = True

    db.commit()

    return {"message": "Password reset successful"}
