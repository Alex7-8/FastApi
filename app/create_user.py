# app/create_user.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .auth import verify_token
from .entrenamiento_bcrypt import hash_password
from app.dependencies import Usuario, get_db  # <--- AHORA desde dependencies.py

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/", tags=["usuarios"])
def crear_usuario(user: UserCreate, db: Session = Depends(get_db), current_user: str = Depends(verify_token)):
    db_user = db.query(Usuario).filter(Usuario.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_pwd = hash_password(user.password)
    nuevo_usuario = Usuario(username=user.username, password=hashed_pwd)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"message": "Usuario creado exitosamente", "username": nuevo_usuario.username}
