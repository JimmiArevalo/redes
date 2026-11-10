import os
import socket

from fastapi import FastAPI

app = FastAPI(title="API de Servidores Docker")

# Variable de entorno que diferencia cada instancia
SERVIDOR = os.getenv("SERVIDOR", "Servidor sin nombre")


@app.get("/")
def inicio():
    return {
        "mensaje": "El servidor está funcionando correctamente",
        "servidor": SERVIDOR,
        "hostname_contenedor": socket.gethostname(),
    }


@app.get("/salud")
def salud():
    return {
        "estado": "activo",
        "servidor": SERVIDOR,
    }