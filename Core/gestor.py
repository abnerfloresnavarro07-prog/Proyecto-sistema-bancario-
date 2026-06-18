import json
import os

FILE_PATH = "data/datos.json"

def cargar_datos():

    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_datos(datos):

    with open(FILE_PATH, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def listar_cuentas():
    return cargar_datos()


def crear_cuenta(nueva_cuenta):

    datos = cargar_datos()

    for cuenta in datos:
        if cuenta["numero_cuenta"] == nueva_cuenta["numero_cuenta"]:
            return False, "El número de cuenta ya existe."

    if datos:
        nueva_cuenta["id"] = datos[-1]["id"] + 1
    else:
        nueva_cuenta["id"] = 1

    datos.append(nueva_cuenta)

    guardar_datos(datos)

    return True, "Cuenta creada correctamente."


def buscar_cuenta(numero_cuenta):

    datos = cargar_datos()

    for cuenta in datos:

        if cuenta["numero_cuenta"] == numero_cuenta:
            return cuenta

    return None


def actualizar_cuenta(numero_cuenta, datos_actualizados):

    datos = cargar_datos()

    for i, cuenta in enumerate(datos):

        if cuenta["numero_cuenta"] == numero_cuenta:

            datos_actualizados["id"] = cuenta["id"]
            datos_actualizados["numero_cuenta"] = numero_cuenta

            datos[i] = datos_actualizados

            guardar_datos(datos)

            return True

    return False


def eliminar_cuenta(numero_cuenta):

    datos = cargar_datos()

    datos = [
        cuenta
        for cuenta in datos
        if cuenta["numero_cuenta"] != numero_cuenta
    ]

    guardar_datos(datos)

    return True


def depositar(numero_cuenta, monto):

    datos = cargar_datos()

    for cuenta in datos:

        if cuenta["numero_cuenta"] == numero_cuenta:

            cuenta["saldo"] += monto

            guardar_datos(datos)

            return True

    return False


def retirar(numero_cuenta, monto):

    datos = cargar_datos()

    for cuenta in datos:

        if cuenta["numero_cuenta"] == numero_cuenta:

            if monto > cuenta["saldo"]:
                return False

            cuenta["saldo"] -= monto

            guardar_datos(datos)

            return True

    return False