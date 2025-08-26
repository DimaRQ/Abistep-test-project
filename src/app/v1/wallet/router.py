from fastapi import APIRouter, HTTPException, status

from src.app.v1.wallet import schemas
from src.db.session import db

router = APIRouter(prefix="/wallet", tags=["Wallet"])


@router.post("/transfer/")
async def transfer(data: schemas.TransferIn):
    from_user = db.users.get(data.from_user_id)
    to_user = db.users.get(data.to_user_id)

    if not from_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Пользователь {data.from_user_id} не найден",
        )
    if not to_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Пользователь {data.to_user_id} не найден",
        )
    if data.from_user_id == data.to_user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Нельзя переводить себе"
        )
    if from_user.get("balance", 0) < data.amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Недостаточно средств"
        )

    from_user["balance"] -= data.amount
    to_user["balance"] += data.amount

    return {"status": "ok"}
