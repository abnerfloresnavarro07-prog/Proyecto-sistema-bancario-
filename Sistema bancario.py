cuentas = {}

# Crear cuentas
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


# Mostrar saldo
def mostrar_saldo(numero_cuenta):

    print(f"\nCliente: {cuentas[numero_cuenta]['nombre']}")
    print(f"Saldo actual: {cuentas[numero_cuenta]['saldo']:.2f} C$")


# Depositar dinero
def depositar(numero_cuenta):

    monto = float(input("Ingrese el monto a depositar: "))

    if monto < 0:
        print("El monto no puede ser negativo.")

    else:
        cuentas[numero_cuenta]["saldo"] += monto
        print("Depósito realizado con éxito.")

def retirar(numero_cuenta):

    monto = float(input("Ingrese el monto a retirar: "))

    if monto < 0:
        print("El monto no puede ser negativo.")

    elif monto > cuentas[numero_cuenta]["saldo"]:
        print("No tienes suficiente saldo.")

    else:
        cuentas[numero_cuenta]["saldo"] -= monto
        print("Retiro realizado con éxito.")


def menu_principal():

    print("\n===== SISTEMA BANCARIO =====")
    print("1. Mostrar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Cerrar sesión")
    print("5. Salir del sistema")

    opcion = input("Seleccione una opción: ")

    return opcion


def main():

    while True:

        print("\n===== INICIO DE SESIÓN =====")

        numero_cuenta = input("Ingrese su número de cuenta: ")
        cedula = input("Ingrese su cédula: ")

        # Verificar cuenta
        if numero_cuenta not in cuentas:
            print("Número de cuenta no encontrado.")
            continue

        # Verificar cédula
        if cuentas[numero_cuenta]["cedula"] != cedula:
            print("Cédula incorrecta.")
            continue

        print(f"\nBienvenido/a {cuentas[numero_cuenta]['nombre']}")

        while True:

            opcion = menu_principal()

            if opcion == '1':
                mostrar_saldo(numero_cuenta)

            elif opcion == '2':
                depositar(numero_cuenta)

            elif opcion == '3':
                retirar(numero_cuenta)

            elif opcion == '4':
                print("Cerrando sesión...")
                break

            elif opcion == '5':
                print("Agradecemos por usar el sistema bancario.")
            
                return
            
            else:
                print("Opción inválida.")
if __name__ == "__main__":
    main()