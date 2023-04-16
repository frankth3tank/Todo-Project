import models
from fastapi import FastAPI, Depends, HTTPException
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()

@app.get("/todo/{id}")
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()

def http_exception():
    raise HTTPException(status_code = 404, detail = "Todo not found")
