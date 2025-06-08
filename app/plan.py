from datetime import datetime, timedelta

fecha_inicio = datetime.today()
tareas = ["diseño_db", "login_api", "hashing", "pytest", "CI"]
plan = {t: fecha_inicio + timedelta(days=i*2) for i, t in enumerate(tareas)}
for tarea, fecha in plan.items():
    print(f"{tarea}: {fecha.strftime('%Y-%m-%d')}")
