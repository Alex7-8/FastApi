#app/entrenamiento_bcrypt.py
import bcrypt

def hash_password(password: str) -> str:
    """Genera un hash seguro a partir de una contraseña en texto plano."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña coincide con su hash."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

