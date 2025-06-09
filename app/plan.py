#app/plan.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from pydantic import BaseModel
from datetime import datetime, timedelta
from .auth import verify_token

# Definir el modelo de entrada para recibir el plan de tareas
class PlanTareas(BaseModel):
    tareas: Dict[str, str]  # Tareas con sus fechas de inicio en formato string

# Definir el modelo de salida para enviar la información procesada
class PlanRespuesta(BaseModel):
    tarea: str
    fecha_inicio: str

router = APIRouter()

@router.post("/plan/", response_model=List[PlanRespuesta], tags=["plan"])
def obtener_plan_data(plan_tareas: PlanTareas, user: str = Depends(verify_token)):
    """
    Recibe un JSON con las tareas y sus fechas de inicio, y devuelve la información procesada.
    """
    # Convertir las fechas de inicio desde string a datetime
    tareas_con_fechas = []
    for tarea, fecha_str in plan_tareas.tareas.items():
        try:
            fecha_inicio = datetime.strptime(fecha_str, "%Y-%m-%d")
            tareas_con_fechas.append(PlanRespuesta(tarea=tarea, fecha_inicio=fecha_inicio.strftime("%Y-%m-%d")))
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Formato de fecha inválido para la tarea {tarea}. Debe ser 'YYYY-MM-DD'.")

    return tareas_con_fechas
