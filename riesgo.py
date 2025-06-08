# riesgo.py
import subprocess

print("Analizando dependencias con Bandit...")
subprocess.run(["bandit", "-r", "app/"])

print("Verificando CVEs con Safety...")
subprocess.run(["safety", "check", "--full-report"])
