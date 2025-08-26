from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str = Field(..., examples=["Dmitry"])
    email: EmailStr = Field(..., examples=["dmitry@gmail.com"])


class UserCreate(UserBase):
    balance: Decimal = Field(default=0, ge=0, examples=["100.00"])


class UserOut(UserBase):
    id: int = Field(..., examples=[1])
    balance: Decimal = Field(..., examples=["99.85"])

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Dmitry",
                "email": "dmitry@gmail.com",
                "balance": "99.85",
            }
        }
