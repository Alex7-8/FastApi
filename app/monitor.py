# app/monitor.py
planeadas = {
    "diseño_db": 1,
    "login_api": 1,
    "hashing": 1,
    "pytest": 1,
    "CI": 1,
    "validaciones_input": 1,
    "autenticacion_token": 1
}

completadas = {
    "diseño_db": 1,
    "login_api": 1,
    "pytest": 1,
    "validaciones_input": 1
}

total_planeadas = len(planeadas)
total_completadas = len(completadas)

avance = (total_completadas / total_planeadas) * 100
print(f"Progreso actual del proyecto: {avance:.2f}%")
