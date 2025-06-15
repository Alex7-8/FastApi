# app/incidentes.py
from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Incidente as IncidenteDB, AccionCorrectiva as AccionCorrectivaDB

router = APIRouter()

# Modelos Pydantic
class Incidente(BaseModel):
    error: str
    causa: str
    class Config:
        orm_mode = True

class AccionCorrectiva(BaseModel):
    descripcion: str
    aplicada: bool
    class Config:
        orm_mode = True

# Endpoints

@router.get("/incidentes/", response_model=List[Incidente])
def obtener_incidentes(db: Session = Depends(get_db)):
    return db.query(IncidenteDB).all()

@router.get("/acciones/", response_model=List[AccionCorrectiva])
def obtener_acciones(db: Session = Depends(get_db)):
    return db.query(AccionCorrectivaDB).all()

@router.post("/incidentes/")
def registrar_incidente(incidente: Incidente, db: Session = Depends(get_db)):
    nuevo = IncidenteDB(error=incidente.error, causa=incidente.causa)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Incidente registrado correctamente", "id": nuevo.id}

@router.post("/acciones/")
def registrar_accion(accion: AccionCorrectiva, db: Session = Depends(get_db)):
    nueva = AccionCorrectivaDB(descripcion=accion.descripcion, aplicada=accion.aplicada)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return {"mensaje": "Acción correctiva registrada", "id": nueva.id}
