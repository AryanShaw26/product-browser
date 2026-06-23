from faker import Faker
from datetime import datetime, timedelta
from random import choice, uniform
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Product

fake = Faker()

CATEGORIES = [
    "Electronics",
    "Books",
    "Fashion",
    "Sports",
    "Home"
]

BATCH_SIZE = 5000
TOTAL_PRODUCTS = 200000


def generate_products():
    db: Session = SessionLocal()

    try:
        for start in range(0, TOTAL_PRODUCTS, BATCH_SIZE):

            products = []

            for _ in range(BATCH_SIZE):

                created_at = fake.date_time_between(
                    start_date="-2y",
                    end_date="now"
                )

                updated_at = created_at + timedelta(
                    days=uniform(0, 365)
                )

                products.append(
                    Product(
                        name=fake.word().title() + " Product",
                        category=choice(CATEGORIES),
                        price=round(uniform(100, 5000), 2),
                        created_at=created_at,
                        updated_at=updated_at
                    )
                )

            db.bulk_save_objects(products)
            db.commit()

            print(
                f"Inserted {start + BATCH_SIZE} products..."
            )

    finally:
        db.close()


if __name__ == "__main__":
    generate_products()