from core.gestor import *

def menu():
    while True:
        print("\n===== SISTEMA BANCARIO =====")
        print("1. Crear cuenta")
        print("2. Listar cuentas")
        print("3. Buscar cuenta")
        print("4. Depositar")
        print("5. Retirar")
        print("6. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            cedula = input("Cédula: ")
            numero_cuenta = input("Número de cuenta: ")

            resultado = crear_cuenta({
                "nombre": nombre,
                "cedula": cedula,
                "numero_cuenta": numero_cuenta
            })

            print(resultado)


        elif op == "2":
            cuentas = listar_cuentas()
            for c in cuentas:
                print(c)


        elif op == "3":
            num = input("Número de cuenta: ")
            resultado = buscar_cuenta(num)
            print(resultado if resultado else "No encontrada")


        elif op == "4":
            num = input("Número de cuenta: ")
            monto = float(input("Monto a depositar: "))
            print(depositar(num, monto))


        elif op == "5":
            num = input("Número de cuenta: ")
            monto = float(input("Monto a retirar: "))
            print(retirar(num, monto))


        elif op == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")