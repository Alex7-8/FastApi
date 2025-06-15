# gov_policies.py
from datetime import datetime
class Politica:
    def __init__(self, id, nombre, descripcion, responsable, fecha_revision):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.responsable = responsable
        self.fecha_revision = fecha_revision
# Simulación de políticas activas
politicas_activas = [
    Politica(1, "Seguridad de la Información", "Control de acceso, tokens y cifrado", "CISO", datetime(2025, 5, 10)),
    Politica(2, "Calidad de Software", "Cobertura mínima de pruebas 90%, revisión de código obligatoria", "CTO", datetime(2025, 6, 1)),
]

# Auditoría de cumplimiento
def auditoria_politicas():
    print("Políticas activas y fecha de última revisión:")
    for p in politicas_activas:
        print(f"- {p.nombre} ({p.responsable}) - Revisada el {p.fecha_revision.date()}")

auditoria_politicas()

