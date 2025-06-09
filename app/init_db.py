from app.db import engine, Base
from app.models import User, LoginAttempt, Incidente, AccionCorrectiva, Progreso

# Crear las tablas
Base.metadata.create_all(bind=engine)
