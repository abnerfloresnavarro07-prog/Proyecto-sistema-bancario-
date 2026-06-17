cuentas = {}

cantidad = int(input("¿Cuántas cuentas desea crear?: "))

for i in range(cantidad):

    nombre = input("Ingrese el nombre: ")
    cedula = input("Ingrese la cédula: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")

    cuentas[numero_cuenta] = {
        "nombre": nombre,
        "cedula": cedula,
        "saldo": 0
    }


def mostrar_saldo(numero_cuenta):

    print(f"\nCliente: {cuentas[numero_cuenta]['nombre']}")
    print(f"Saldo actual: {cuentas[numero_cuenta]['saldo']:.2f} C$")


def depositar(numero_cuenta):

    monto = float(input("Ingrese el monto a depositar: "))

    if monto <= 0:
        print("El monto debe ser mayor que cero.")
    else:
        cuentas[numero_cuenta]["saldo"] += monto
        print("Depósito realizado con éxito.")


def retirar(numero_cuenta):

    monto = float(input("Ingrese el monto a retirar: "))

    if monto <= 0:
        print("El monto debe ser mayor que cero.")

    elif monto > cuentas[numero_cuenta]["saldo"]:
        print("No tienes suficiente saldo.")

    else:
        cuentas[numero_cuenta]["saldo"] -= monto
        print("Retiro realizado con éxito.")


def eliminar_cuenta(numero_cuenta):

    confirmar = input("¿Está seguro de eliminar su cuenta? (S/N): ")

    if confirmar.upper() == "S":

        del cuentas[numero_cuenta]

        print("Cuenta eliminada correctamente.")

        crear = input("¿Desea crear una nueva cuenta? (S/N): ")

        if crear.upper() == "S":

            nombre = input("Ingrese el nombre: ")
            cedula = input("Ingrese la cédula: ")
            nueva_cuenta = input("Ingrese el número de cuenta: ")

            cuentas[nueva_cuenta] = {
                "nombre": nombre,
                "cedula": cedula,
                "saldo": 0
            }

            print("Nueva cuenta creada correctamente.")

        return True

    else:
        print("Operación cancelada.")
        return False



def menu_principal():

    print("\n===== SISTEMA BANCARIO =====")
    print("1. Mostrar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Eliminar cuenta")
    print("5. Cerrar sesión")
    print("6. Salir del sistema")

    return input("Seleccione una opción: ")


def main():

    while True:

        print("\n===== INICIO DE SESIÓN =====")

        numero_cuenta = input("Ingrese su número de cuenta: ")
        cedula = input("Ingrese su cédula: ")

        if numero_cuenta not in cuentas:
            print("Número de cuenta no encontrado.")
            continue

        if cuentas[numero_cuenta]["cedula"] != cedula:
            print("Cédula incorrecta.")
            continue

        print(f"\nBienvenido/a {cuentas[numero_cuenta]['nombre']}")

        while True:

            opcion = menu_principal()

            if opcion == "1":
                mostrar_saldo(numero_cuenta)

            elif opcion == "2":
                depositar(numero_cuenta)

            elif opcion == "3":
                retirar(numero_cuenta)

            elif opcion == "4":

                eliminar = eliminar_cuenta(numero_cuenta)

                if eliminar:
                    break

            elif opcion == "5":
                print("Cerrando sesión...")
                break

            elif opcion == "6":
                print("Gracias por usar el sistema bancario.")
                return

            else:
                print("Opción inválida.")


if __name__ == "__main__":
    main()