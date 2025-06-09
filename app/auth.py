# app/auth.py

from fastapi import Header, HTTPException
from datetime import datetime, timedelta
import bcrypt

login_attempts = {}
BLOCK_DURATION = timedelta(minutes=15)
MAX_ATTEMPTS = 5

def is_user_blocked(username: str) -> bool:
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    if data["blocked_until"] and datetime.now() < data["blocked_until"]:
        return True
    return False

def register_login_attempt(username: str, success: bool):
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    if success:
        login_attempts[username] = {"attempts": 0, "blocked_until": None}
    else:
        data["attempts"] += 1
        if data["attempts"] >= MAX_ATTEMPTS:
            data["blocked_until"] = datetime.now() + BLOCK_DURATION
        login_attempts[username] = data

def login(username: str, password: str):
    if is_user_blocked(username):
        raise HTTPException(status_code=403, detail="Usuario bloqueado temporalmente.")

    stored_password_hash = bcrypt.hashpw("secret".encode(), bcrypt.gensalt())
    success = bcrypt.checkpw(password.encode(), stored_password_hash)

    register_login_attempt(username, success)

    if not success:
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")

    return {"msg": "Login exitoso"}

def verify_token(authorization: str = Header(...)) -> str:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")

    token = authorization.replace("Bearer ", "")
    
    # Simulación básica de validación
    if token != "123456":  # Aquí iría la validación real
        raise HTTPException(status_code=401, detail="Token inválido")

    return "usuario_validado"