import json
import os

RUTA = os.path.join("Data", "datos.json")
os.makedirs("Data", exist_ok=True)


def cargar_datos():
    if not os.path.exists(RUTA):
        return {}
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return {}


def guardar_datos(cuentas):
    with open(RUTA, "w", encoding="utf-8") as archivo:
        json.dump(cuentas, archivo, indent=4, ensure_ascii=False)


cuentas = cargar_datos()


def crear_cuenta(nombre, cedula, numero_cuenta):
    if numero_cuenta in cuentas:
        return "EXISTE"

    cuentas[numero_cuenta] = {
        "nombre": nombre,
        "cedula": cedula,
        "saldo": 0
    }

    guardar_datos(cuentas)
    return "OK"


def iniciar_sesion(numero_cuenta, cedula):
    if numero_cuenta not in cuentas:
        return False
    return cuentas[numero_cuenta]["cedula"] == cedula


def mostrar_saldo(numero_cuenta):
    if numero_cuenta not in cuentas:
        return None
    return cuentas[numero_cuenta]["saldo"]


def depositar(numero_cuenta, monto):
    if numero_cuenta not in cuentas:
        return "NO_CUENTA"
    if monto <= 0:
        return "INVALIDO"

    cuentas[numero_cuenta]["saldo"] += monto
    guardar_datos(cuentas)
    return cuentas[numero_cuenta]["saldo"]


def retirar(numero_cuenta, monto):
    if numero_cuenta not in cuentas:
        return "NO_CUENTA"
    if monto <= 0:
        return "INVALIDO"
    if monto > cuentas[numero_cuenta]["saldo"]:
        return "INSUFICIENTE"

    cuentas[numero_cuenta]["saldo"] -= monto
    guardar_datos(cuentas)
    return cuentas[numero_cuenta]["saldo"]


def eliminar_cuenta(numero_cuenta):
    if numero_cuenta not in cuentas:
        return False

    del cuentas[numero_cuenta]
    guardar_datos(cuentas)
    return True


def listar_cuentas():
    return cuentas