from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from .auth import verify_token

# Definir el modelo de entrada para recibir las tareas
class Tareas(BaseModel):
    planeadas: Dict[str, int]
    completadas: Dict[str, int]

# Definir el modelo de salida para enviar la información procesada
class Avance(BaseModel):
    total_planeadas: int
    total_completadas: int
    avance: float
    tareas_planeadas: Dict[str, int]
    tareas_completadas: Dict[str, int]

router = APIRouter()

@router.post("/monitor/", response_model=Avance, tags=["monitor"])
def obtener_monitor_data(tareas: Tareas, user: str = Depends(verify_token)):
    """
    Recibe un JSON con las tareas planeadas y completadas, calcula el avance y 
    devuelve la información procesada.
    """
    total_planeadas = len(tareas.planeadas)
    total_completadas = len(tareas.completadas)

    if total_planeadas == 0:  # Evitar división por cero
        raise HTTPException(status_code=400, detail="No hay tareas planeadas.")

    avance = (total_completadas / total_planeadas) * 100

    # Devolver la información procesada en un JSON
    return Avance(
        total_planeadas=total_planeadas,
        total_completadas=total_completadas,
        avance=avance,
        tareas_planeadas=tareas.planeadas,
        tareas_completadas=tareas.completadas
    )
