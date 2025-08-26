from decimal import Decimal

from pydantic import BaseModel, Field


class TransferIn(BaseModel):
    from_user_id: int = Field(..., ge=1, examples=[1])
    to_user_id: int = Field(..., ge=1, examples=[2])
    amount: Decimal = Field(..., gt=0, examples=["50.00"])

    @classmethod
    def normalize_amount(cls, v: Decimal) -> Decimal:
        return v.quantize(Decimal("0.01"))


class TransferOut(BaseModel):
    status: str = Field(..., examples=["ok"])
