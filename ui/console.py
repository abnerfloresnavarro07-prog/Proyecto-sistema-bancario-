from core.gestor import *


def menu():

    while True:

        print("\n===== SISTEMA BANCARIO =====")

        print("1. Listar cuentas")
        print("2. Crear cuenta")
        print("3. Buscar cuenta")
        print("4. Actualizar cuenta")
        print("5. Eliminar cuenta")
        print("6. Depositar")
        print("7. Retirar")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        # LISTAR

        if opcion == "1":

            cuentas = listar_cuentas()

            if not cuentas:
                print("No existen cuentas.")
            else:

                for cuenta in cuentas:

                    print(
                        f"ID:{cuenta['id']} | "
                        f"Cuenta:{cuenta['numero_cuenta']} | "
                        f"Nombre:{cuenta['nombre']} | "
                        f"Saldo:{cuenta['saldo']}"
                    )

        # CREAR

        elif opcion == "2":

            nombre = input("Nombre: ")
            cedula = input("Cedula: ")
            numero = input("Numero de cuenta: ")

            exito, mensaje = crear_cuenta({

                "nombre": nombre,
                "cedula": cedula,
                "numero_cuenta": numero,
                "saldo": 0

            })

            print(mensaje)

        # BUSCAR

        elif opcion == "3":

            numero = input("Numero de cuenta: ")

            cuenta = buscar_cuenta(numero)

            if cuenta:

                print(cuenta)

            else:

                print("Cuenta no encontrada.")

        # ACTUALIZAR

        elif opcion == "4":

            numero = input("Numero de cuenta: ")

            cuenta = buscar_cuenta(numero)

            if cuenta:

                nombre = input("Nuevo nombre: ")
                cedula = input("Nueva cedula: ")

                actualizar_cuenta(numero, {

                    "nombre": nombre,
                    "cedula": cedula,
                    "saldo": cuenta["saldo"]

                })

                print("Cuenta actualizada.")

            else:

                print("Cuenta no encontrada.")

        # ELIMINAR

        elif opcion == "5":

            numero = input("Numero de cuenta: ")

            eliminar_cuenta(numero)

            print("Cuenta eliminada.")

        # DEPOSITAR

        elif opcion == "6":

            numero = input("Numero de cuenta: ")

            try:

                monto = float(input("Monto a depositar: "))

                if monto <= 0:
                    print("El monto debe ser mayor a cero.")
                else:

                    depositar(numero, monto)

                    print("Deposito realizado.")

            except ValueError:

                print("Debe ingresar un número.")

        # RETIRAR

        elif opcion == "7":

            numero = input("Numero de cuenta: ")

            try:

                monto = float(input("Monto a retirar: "))

                resultado = retirar(numero, monto)

                if resultado:
                    print("Retiro exitoso.")
                else:
                    print("Saldo insuficiente.")

            except ValueError:

                print("Debe ingresar un número.")

        # SALIR

        elif opcion == "8":

            print("Gracias por usar el sistema.")

            break

        else:

            print("Opción inválida.")