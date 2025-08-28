from fastapi import APIRouter, Depends
from fastapi import status, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from messenger.schemas.user import CreateUser, UserOut
from messenger.modules.db import get_db
from messenger.models.users import Users

router = APIRouter(
        prefix="/user"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: CreateUser, db: AsyncSession = Depends(get_db)):
    new_user = Users(**user.dict()) 

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)  

    return new_user

@router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await db.get(Users, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
