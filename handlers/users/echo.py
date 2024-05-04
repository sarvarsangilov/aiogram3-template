import logging
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def echo(message: Message):

    await message.send_copy(chat_id=message.from_user.id)
