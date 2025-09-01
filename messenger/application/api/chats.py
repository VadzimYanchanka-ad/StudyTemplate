from fastapi import APIRouter, Depends
from fastapi import status, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from messenger.schemas.chat import CreateChat, ChatOut
from messenger.schemas.chat_user import ChatUserOut

from messenger.modules.db import get_db

from messenger.models.chats import Chats
from messenger.models.chat_user import ChatUser

router = APIRouter(prefix="/chat")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ChatOut)
async def create_chat(chat: CreateChat, db: AsyncSession = Depends(get_db)):
    chat_room = Chats.from_request(chat)

    db.add(chat_room)

    await db.commit()
    await db.refresh(chat_room)

    return chat_room

@router.post("/{chat_id}/{user_id}", status_code=status.HTTP_200_OK, response_model=ChatUserOut)
async def add_user_to_chat(chat_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    if await db.get(ChatUser, {"chat_id": chat_id, "user_id": user_id}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already in chat")
    
    new_user = ChatUser(chat_id=chat_id, user_id=user_id)

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.delete("/{chat_id}/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user_from_chat(chat_id: int, user_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(ChatUser).where(
        ChatUser.chat_id == chat_id,
        ChatUser.user_id == user_id
    )
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        await db.delete(user)
        await db.commit()
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="already delete")
    