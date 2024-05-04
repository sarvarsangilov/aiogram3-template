from aiogram import Router

router = Router()

from . import groups, users, channels

router.include_routers(groups.router, users.router, channels.router)
