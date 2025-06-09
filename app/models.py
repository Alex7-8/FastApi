from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

# Modelo de Usuario
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    disabled = Column(Boolean, default=False)

# Modelo de Intentos de Inicio de Sesión
class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    success = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String)

# Modelo de Incidente
class Incidente(Base):
    __tablename__ = "incidentes"
    
    id = Column(Integer, primary_key=True, index=True)
    error = Column(String)
    causa = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Modelo de Acción Correctiva
class AccionCorrectiva(Base):
    __tablename__ = "acciones_correctivas"
    
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    aplicada = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Modelo de Progreso del Proyecto
class Progreso(Base):
    __tablename__ = "progreso"
    
    id = Column(Integer, primary_key=True, index=True)
    tarea = Column(String)
    status = Column(String, default="planeada")
    fecha_inicio = Column(DateTime, default=datetime.utcnow)
    fecha_fin = Column(DateTime, nullable=True)
