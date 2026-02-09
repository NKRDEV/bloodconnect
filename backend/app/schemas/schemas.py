from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum
from typing import Optional


class UserRole(str, Enum):
    DONOR = "donor"
    RECIPIENT = "recipient"
    ADMIN = "admin"


class BloodType(str, Enum):
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"


class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone: str
    #role: UserRole = UserRole.DONOR
    blood_type: Optional[BloodType] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    blood_type: Optional[BloodType] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class BloodRequestBase(BaseModel):
    blood_type: BloodType
    quantity: int


class BloodRequestCreate(BloodRequestBase):
    pass


class BloodRequestUpdate(BaseModel):
    status: Optional[str] = None
    quantity: Optional[int] = None


class BloodRequestResponse(BloodRequestBase):
    id: int
    status: str
    created_by: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DonationBase(BaseModel):
    blood_type: BloodType
    quantity: int


class DonationCreate(DonationBase):
    donor_id: int


class DonationResponse(DonationBase):
    id: int
    donor_id: int
    donation_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class ForgotPasswordRequest(BaseModel):
    email:EmailStr

class ResetPasswordRequest(BaseModel):
    token:str
    new_password:str