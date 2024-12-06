# app/schemas.py
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    monthly_income: float

    @validator('monthly_income')
    def check_positive_income(cls, v):
        if v <= 0:
            raise ValueError('Monthly income must be positive')
        return v

# app/models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    monthly_income = Column(Float)