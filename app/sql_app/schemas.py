from pydantic import BaseModel


class PaymentPayload(BaseModel):
    PaymentMethodId: int
    InvoiceValue: float


class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True
