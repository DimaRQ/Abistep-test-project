from fastapi import APIRouter

from src.app.v1.user.router import router as user_router
from src.app.v1.wallet.router import router as wallet_router

router = APIRouter(prefix="/v1")
router.include_router(user_router)
router.include_router(wallet_router)
