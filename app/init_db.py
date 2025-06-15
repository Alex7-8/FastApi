from app.db import engine, Base
from app.models import User, LoginAttempt, Incidente, AccionCorrectiva, Progreso

# Crear las tablas
def create_tables():
    """Crea las tablas en la base de datos."""
Base.metadata.create_all(bind=engine, tables=[User.__table__, LoginAttempt.__table__, Incidente.__table__, AccionCorrectiva.__table__, Progreso.__table__])