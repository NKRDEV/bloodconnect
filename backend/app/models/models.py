from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from app.database.database import Base
import enum


class UserRole(str, enum.Enum):
    DONOR = "donor"
    RECIPIENT = "recipient"
    ADMIN = "admin"


class BloodType(str, enum.Enum):
    O_POSITIVE = "O+"
    O_NEGATIVE = "O-"
    A_POSITIVE = "A+"
    A_NEGATIVE = "A-"
    B_POSITIVE = "B+"
    B_NEGATIVE = "B-"
    AB_POSITIVE = "AB+"
    AB_NEGATIVE = "AB-"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    phone = Column(String)
    role = Column(Enum(UserRole), default=UserRole.DONOR)
    blood_type = Column(Enum(BloodType), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True, index=True)
    blood_type = Column(Enum(BloodType))
    quantity = Column(Integer)  # in ml
    status = Column(String, default="pending")  # pending, fulfilled, cancelled
    created_by = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Donation(Base):
    __tablename__ = "donations"

    id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer)
    blood_type = Column(Enum(BloodType))
    quantity = Column(Integer)  # in ml
    donation_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
