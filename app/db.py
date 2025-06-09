from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos (SQLite por defecto)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Aquí usas SQLite en un archivo local

# Crear motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base para definir modelos
Base = declarative_base()

# Función para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
