from doctest import Example

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr = Field(..., example="email@dominio.com")
    username: str = Field(..., min_length=3, max_length=50, example="userExample")


class User(UserBase):
    id: int = Field(..., example="5")


class UserRegister(UserBase):
    password: str = Field(..., min_length=8, max_length=64, example="strongpass")
