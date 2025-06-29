from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.dbutils import get_db
from models.models import User
from models.schemas import CreateUserSchema

router = APIRouter()

@router.post("/create")
def create_user(payload: CreateUserSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(
        name=payload.name,
        email=payload.email
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "message": "User created successfully",
        "user_id": new_user.user_id,
        "email": new_user.email
    }