from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from datetime import datetime

from app.database import get_db
from app.models import Product
from app.utils import encode_cursor, decode_cursor
from app.schemas import ProductListResponse
router = APIRouter()


@router.get("/products",
            response_model=ProductListResponse
)
def get_products(
    limit: int = 20,
    cursor: str = None,
    category: str = None,
    snapshot: str = None,
    db: Session = Depends(get_db)
):
    
    query = db.query(Product)

    # Snapshot handling
    if snapshot:
        snapshot_time = datetime.fromisoformat(snapshot)
    else:
        snapshot_time = datetime.utcnow()

    # Freeze dataset for current browsing session
    query = query.filter(
        Product.updated_at <= snapshot_time
    )

    # Category filter
    if category:
        query = query.filter(
            Product.category == category
        )

    # Cursor pagination
    if cursor:
        cursor_data = decode_cursor(cursor)

        cursor_time = datetime.fromisoformat(
            cursor_data["updated_at"]
        )

        cursor_id = cursor_data["id"]

        query = query.filter(
            or_(
                Product.updated_at < cursor_time,
                and_(
                    Product.updated_at == cursor_time,
                    Product.id < cursor_id
                )
            )
        )

    products = (
        query
        .order_by(
            Product.updated_at.desc(),
            Product.id.desc()
        )
        .limit(limit)
        .all()
    )

    next_cursor = None

    if products:
        last_product = products[-1]

        next_cursor = encode_cursor(
            last_product.updated_at,
            last_product.id
        )

    return {
        "products": products,
        "next_cursor": next_cursor,
        "snapshot": snapshot_time.isoformat()
    }