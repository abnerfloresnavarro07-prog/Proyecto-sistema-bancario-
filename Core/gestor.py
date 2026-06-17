import json
import os

FILE_PATH = "data/datos.json"


# -------------------------
# CARGAR Y GUARDAR
# -------------------------
def cargar_datos():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_datos(datos):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


# -------------------------
# CRUDL
# -------------------------
def listar_cuentas():
    return cargar_datos()


def buscar_cuenta(numero_cuenta):
    datos = cargar_datos()
    for c in datos:
        if c["numero_cuenta"] == numero_cuenta:
            return c
    return None


def crear_cuenta(cuenta):
    datos = cargar_datos()

    # Validación: cuenta única
    for c in datos:
        if c["numero_cuenta"] == cuenta["numero_cuenta"]:
            return "ERROR: La cuenta ya existe"

    cuenta["saldo"] = 0.0
    datos.append(cuenta)
    guardar_datos(datos)
    return "Cuenta creada exitosamente"


def depositar(numero_cuenta, monto):
    datos = cargar_datos()

    for c in datos:
        if c["numero_cuenta"] == numero_cuenta:
            if monto <= 0:
                return "ERROR: Monto inválido"

            c["saldo"] += monto
            guardar_datos(datos)
            return "Depósito exitoso"

    return "ERROR: Cuenta no encontrada"


def retirar(numero_cuenta, monto):
    datos = cargar_datos()

    for c in datos:
        if c["numero_cuenta"] == numero_cuenta:

            if monto <= 0:
                return "ERROR: Monto inválido"

            if monto > c["saldo"]:
                return "ERROR: Saldo insuficiente"

            c["saldo"] -= monto
            guardar_datos(datos)
            return "Retiro exitoso"

    return "ERROR: Cuenta no encontrada"