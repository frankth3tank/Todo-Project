from models import Todos
from fastapi import APIRouter, Depends, HTTPException 
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Annotated, Optional
from starlette import status
from .auth import get_current_user

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
        
class Todo(BaseModel):
    title : str
    description : Optional[str]
    priority : int = Field(gt=0, lt=6, description="Priority must be between 1-5")
    complete: bool
    
        
@router.get("/", status_code = status.HTTP_200_OK)
async def read_all(user: user_dependency ,db: db_dependency):
    return db.query(Todos).filter(Todos.owner_id == user.get("id")).all()

@router.get("/todo/{id}")
async def read_todo(todo_id: int, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo_model is not None:
        return todo_model
    
    raise http_exception()

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency, todo_request: Todo, db: db_dependency):
    
    if user is None:
        raise HTTPException(status_code = 401, detail = "Authentication failed")
    
    todo_model = Todos(**todo_request.dict(), owner_id = user.get("id"))
    
    db.add(todo_model)
    db.commit()
    
    
@router.put("/{todo_id}")
async def update_todo(todo_id: int, todo: Todo, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo_model is None:
        raise http_exception()
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    
    db.add(todo_model)
    db.commit()
    
    return successful_response(200)
    
@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: db_dependency):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    
    if todo_model is None:
        raise http_exception()
    
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()
    
    return successful_response(200)
    
def successful_response(status_code: int):
    return {
        "status": status_code,
        "transaction": "Successful"
    }

def http_exception():
    raise HTTPException(status_code = 404, detail = "Todo not found")


