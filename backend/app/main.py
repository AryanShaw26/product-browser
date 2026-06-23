from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes.products import router as product_router
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Browser API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://product-browser-orcin.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)

@app.get("/")
def home():
    return {
        "message": "API Running Successfully"
    }