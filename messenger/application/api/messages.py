from fastapi import APIRouter, Depends
from fastapi import status, HTTPException

from messenger.schemas.message import MessageCreate, MessageOut, MessageUpdate
from messenger.models.messages import Messages
from messenger.modules.db import get_db

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

router = APIRouter(
        prefix="/message"
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MessageOut)
async def create_message(msg: MessageCreate, db: AsyncSession = Depends(get_db)):    
    new_message = Messages(**msg.dict())

    db.add(new_message)

    await db.commit()
    await db.refresh(new_message)  

    return new_message

@router.get("/{message_id}", response_model=MessageOut)
async def get_message(message_id: int, db: AsyncSession = Depends(get_db)):
    message = await db.get(Messages, message_id)

    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="message not found")
    return message

@router.put("/update/{message_id}", status_code=status.HTTP_200_OK)
async def update_message(message_id: int, updated_message: MessageUpdate, db: AsyncSession = Depends(get_db)):
    message = await get_message(message_id, db)

    if message:
        message.message = updated_message.message

        await db.commit()

        return message
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this message doesnt exist")

@router.delete("/{message_id}", status_code=status.HTTP_200_OK)
async def delete_message(message_id: int, db: AsyncSession = Depends(get_db)):
    message = await get_message(message_id, db)

    if message:
        await db.delete(message)
        await db.commit()
        return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="message doesnt exist")

@router.get("/history/{chat_id}/{user_id}")
async def get_message_history(chat_id: int, user_id:int, db: AsyncSession = Depends(get_db)):
    stmt = select(Messages).where(
        Messages.chat_id == chat_id,
        Messages.user_id == user_id
    )
    result = await db.scalars(stmt)
    messages = result.all()

    return messages
