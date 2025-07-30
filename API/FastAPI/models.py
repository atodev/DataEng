from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID,uuid4
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]

class UserUpdateRequest(BaseModel):
    first_name: Optional[str] 
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
