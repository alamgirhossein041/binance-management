from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

@app.get("/ping")
async def root():
    return {"message": "pong"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)