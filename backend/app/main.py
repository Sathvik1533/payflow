import os
from dotenv import load_dotenv
from fastapi import FastAPI,APIRouter
from app.api.webhooks import router as webhooks_router

load_dotenv()
app=FastAPI()

app.include_router(webhooks_router)
@app.get ("/health")
def health_check():
    return {"status":"ok"}