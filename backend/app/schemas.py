from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: List[ProductResponse]
    next_cursor: Optional[str] = None
    snapshot: str