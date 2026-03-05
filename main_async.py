# ==============================
# IMPORTACIONES
# ==============================

from fastapi import FastAPI, HTTPException  # Import propio del framework
from typing import List
import asyncio  # Import estándar para programación asíncrona

# ==============================
# CREACIÓN DE APP
# ==============================

app = FastAPI()

# ==============================
# VARIABLES GLOBALES
# ==============================

clientes = []  # Lista compartida
contador_clientes = 0  # Variable global contador

# ==============================
# ENDPOINT CREAR CLIENTE
# ==============================

@app.post("/clientes")
async def crear_cliente(nombre: str):
    global contador_clientes  # Permite modificar variable global

    if not nombre.strip():  # Validación básica
        raise HTTPException(status_code=400, detail="Nombre inválido")

    await asyncio.sleep(3)  # Simulación de proceso bancario

    contador_clientes += 1  # Incrementa contador global

    cliente = {
        "id": contador_clientes,
        "nombre": nombre
    }

    clientes.append(cliente)

    return cliente


# ==============================
# LISTAR CLIENTES
# ==============================

@app.get("/clientes", response_model=List[dict])
def listar_clientes():
    return clientes


# ==============================
# OBTENER CLIENTE
# ==============================

@app.get("/clientes/{cliente_id}")
def obtener_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ==============================
# ACTUALIZAR CLIENTE
# ==============================

@app.put("/clientes/{cliente_id}")
def actualizar_cliente(cliente_id: int, nombre: str):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            cliente["nombre"] = nombre
            return cliente

    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# ==============================
# ELIMINAR CLIENTE
# ==============================

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            clientes.remove(cliente)
            return {"mensaje": "Cliente eliminado"}

    raise HTTPException(status_code=404, detail="Cliente no encontrado")