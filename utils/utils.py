# app/utils.py

import logging
import re

# Configuración del logger
logger = logging.getLogger("login_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("login_events.log")
formatter = logging.Formatter("%(asctime)s - IP: %(ip)s - Usuario: %(user)s - Estado: %(status)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Función auxiliar para registrar logs
def log_login_attempt(ip: str, username: str, status: str):
    logger.info("", extra={"ip": ip, "user": username, "status": status})

# Función para validar formato de usuario
def validate_username(username: str) -> bool:
    pattern = r"^[a-zA-Z0-9_]{3,30}$"
    return bool(re.match(pattern, username))
