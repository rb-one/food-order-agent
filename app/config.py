# app/config.py
import os

# Asegúrate de establecer esta variable en tu entorno para mantenerla segura
JWT_SECRET = os.getenv("JWT_SECRET", "mi_clave_secreta_default")
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@db/app_db")

