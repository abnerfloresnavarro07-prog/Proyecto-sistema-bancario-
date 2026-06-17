import gestor

def menu():
    while True:
        print("\n===== BANCO =====")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Ver saldo")
        print("4. Depositar")
        print("5. Retirar")
        print("6. Eliminar cuenta")
        print("7. Listar cuentas")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            numero = input("Número de cuenta: ")
            print(gestor.crear_cuenta(nombre, cedula, numero))

        elif opcion == "2":
            numero = input("Número de cuenta: ")
            cedula = input("Cédula: ")
            print(gestor.iniciar_sesion(numero, cedula))

        elif opcion == "3":
            numero = input("Número de cuenta: ")
            print("Saldo:", gestor.mostrar_saldo(numero))

        elif opcion == "4":
            numero = input("Número de cuenta: ")
            monto = float(input("Monto: "))
            print(gestor.depositar(numero, monto))

        elif opcion == "5":
            numero = input("Número de cuenta: ")
            monto = float(input("Monto: "))
            print(gestor.retirar(numero, monto))

        elif opcion == "6":
            numero = input("Número de cuenta: ")
            print(gestor.eliminar_cuenta(numero))

        elif opcion == "7":
            print(gestor.listar_cuentas())

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()