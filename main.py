import models
from fastapi import FastAPI
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def create_database() -> str:
    return {"Database": "Created"}
