#app/incidentes.py
from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Modelo de incidente
class Incidente(BaseModel):
    id: int
    error: str
    causa: str

class AccionCorrectiva(BaseModel):
    descripcion: str
    aplicada: bool

# Simulación de log de errores
incident_log: List[Incidente] = [
    Incidente(id=1, error="Token expirado", causa="Tiempo corto"),
    Incidente(id=2, error="Token expirado", causa="No se renovó sesión")
]

acciones_correctivas: List[AccionCorrectiva] = [
    AccionCorrectiva(descripcion="Extensión del tiempo de expiración", aplicada=True),
    AccionCorrectiva(descripcion="Implementar renovación automática de token", aplicada=True)
]

@router.get("/incidentes/", response_model=List[Incidente])
def obtener_incidentes():
    return incident_log

@router.get("/acciones/", response_model=List[AccionCorrectiva])
def obtener_acciones():
    return acciones_correctivas

@router.post("/incidentes/")
def registrar_incidente(incidente: Incidente):
    incident_log.append(incidente)
    return {"mensaje": "Incidente registrado correctamente"}

@router.post("/acciones/")
def registrar_accion(accion: AccionCorrectiva):
    acciones_correctivas.append(accion)
    return {"mensaje": "Acción correctiva registrada"}
