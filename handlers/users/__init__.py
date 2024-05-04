from aiogram import Router
from . import start, echo

router = Router()

routers = [
    start.router,
    echo.router,
]

router.include_routers(start.router, echo.router)
