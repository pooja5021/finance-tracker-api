from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
from enum import Enum


# -----------------------------
# ENUMS
# -----------------------------
class TypeEnum(str, Enum):
    income = "income"
    expense = "expense"


class RoleEnum(str, Enum):
    admin = "admin"
    analyst = "analyst"
    viewer = "viewer"


# -----------------------------
# USER SCHEMAS
# -----------------------------
class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=6)
    role: RoleEnum = RoleEnum.viewer


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes = True


# -----------------------------
# TOKEN SCHEMA
# -----------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


# -----------------------------
# TRANSACTION SCHEMAS
# -----------------------------
class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    type: TypeEnum
    category: str
    date: date   
    notes: Optional[str] = None


class TransactionUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[TypeEnum] = None
    category: Optional[str] = None
    date: Optional[date] = None
    notes: Optional[str] = None


class TransactionOut(BaseModel):
    id: int
    amount: float
    type: TypeEnum
    category: str
    date: date
    notes: Optional[str] = None

    class Config:
        from_attributes = True


# -----------------------------
# ANALYTICS SCHEMA
# -----------------------------
class Summary(BaseModel):
    total_income: float
    total_expenses: float
    current_balance: float
    total_transactions: int