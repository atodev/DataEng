from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import User, Gender, Role,UserUpdateRequest
from uuid import UUID, uuid4
from typing import List, Optional


app = FastAPI()
db: list[User] = [
    User(
        id=uuid4(),
        first_name="Tom",
        last_name="Butler",
        middle_name=None,
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        middle_name="A",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )           
]


@app.get("/")
async def root():
    return {"Hello": "Tom"}   


@app.get("/api/v1/users/")
async def get_users():
    return db

@app.post("/api/v1/users/")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
     for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        
     raise HTTPException(status_code=404, detail=f"User with ID:{user_id} not found")
     
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user_update.first_name is not None:
            user.first_name = user_update.first_name
        if user_update.last_name is not None:
            user.last_name = user_update.last_name
        if user_update.middle_name is not None:
            user.middle_name = user_update.middle_name
        if user_update.roles is not None:
            user.roles = user_update.roles
        return {"message": "User updated successfully", "user": user}
    raise HTTPException(status_code=404, detail=f"User with ID:{user_id} not found")
   