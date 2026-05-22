import os
import mysql.connector

# Intentamos cargar las variables del archivo .env si python-dotenv está instalado
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def obtener_conexion():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),    # Solo el nombre del host
        port=int(os.getenv("DB_PORT", 3306)),      # El puerto va en una línea separada
        user=os.getenv("DB_USER", "root"),         
        password=os.getenv("DB_PASSWORD", ""), 
        database=os.getenv("DB_DATABASE", "modas_ejea_db")
    )