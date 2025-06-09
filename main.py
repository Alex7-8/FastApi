# main.py
from fastapi import FastAPI, Request, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Union
from app.auth import login
from utils.utils import log_login_attempt, validate_username
from app.db import get_db 
from app.incidentes import router as incidentes_router
from app.create_user import router as create_user_router
from app.dependencies import Usuario, get_db




# Configuración de FastAPI
app = FastAPI()

# OAuth2 esquema para extraer el token del header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Importar el router de incidentes
app.include_router(incidentes_router, prefix="/incidentes", tags=["incidentes"])

# Importar el router para crear usuarios
app.include_router(create_user_router, prefix="/usuarios", tags=["usuarios"])

# Clave secreta para JWT y configuraciones de token
SECRET_KEY = "clave_secreta_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Crear token de acceso
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Verificar token de acceso
def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Credenciales no válidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None, user: str = Depends(verify_token)):
    return {"item_id": item_id, "q": q, "user": user}

@app.post("/login")
async def login_route(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")
    ip = request.client.host


    if not validate_username(username):
        log_login_attempt(ip, username, "invalid format")
        return {"error": "Formato de usuario inválido"}

    try:
        user = login(username, password)
        
        # Verificar si el usuario existe en la base de datos
        db_user = db.query(Usuario).filter(Usuario.username == username).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        # Generar el token de acceso
        access_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        log_login_attempt(ip, username, "success")
        
        return {"access_token": access_token, "token_type": "bearer"}
    
    except Exception as e:
        log_login_attempt(ip, username, "failed")
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

