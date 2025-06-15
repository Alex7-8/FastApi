# ii_infrastructure_inventory.py
from datetime import date

class Herramienta:
    def __init__(self, nombre, tipo, version, responsable):
        self.nombre = nombre
        self.tipo = tipo
        self.version = version
        self.responsable = responsable

infraestructura = [
    Herramienta("FastAPI", "Framework Web", "0.95.1", "Backend Team"),
    Herramienta("Docker", "Contenedor", "20.10.7", "DevOps"),
    Herramienta("PostgreSQL", "Base de datos", "15.2", "DBA"),
]

def mostrar_infraestructura():
    print("Infraestructura registrada:")
    for h in infraestructura:
        print(f"- {h.nombre} ({h.tipo}) - Versión: {h.version} - Responsable: {h.responsable}")

mostrar_infraestructura()
