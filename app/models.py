from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    
    @validator("username")
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError("Username must be alphanumeric")
        return v
    @validator("password")
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v
    
class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str
    full_name: Optional[str] = None
    disabled: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None
    roles: List[str] = ["user"]
    
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: bool = False
    created_at: datetime
    roles: List[str] = ["user"]
    
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    
    @validator("password")
    def password_min_length(cls, v):
        if v is not None and len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return v
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Optional[str] = None
    roles: List[str] = ["user"]