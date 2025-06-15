# ii_generate_docs.py
infra_tech_stack = {
    "FastAPI": "0.95.1",
    "Docker": "20.10.7",
    "PostgreSQL": "15.2",
    "Redis": "7.0",
    "Git": "2.40.1"
}

def generar_md():
    with open("TECH_STACK.md", "w") as f:
        f.write("# Documentación de Infraestructura\n\n")
        f.write("| Herramienta | Versión |\n|-------------|---------|\n")
        for herramienta, version in infra_tech_stack.items():
            f.write(f"| {herramienta} | {version} |\n")
    print("Archivo TECH_STACK.md generado.")

generar_md()
