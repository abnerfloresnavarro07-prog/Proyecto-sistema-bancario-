cuentas = {}

# --- C (Create): Crear cuentas ---
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

# --- L (List): Listar todas las cuentas ---
def listar_cuentas():
    print("\n===== LISTA GENERAL DE CUENTAS =====")
    if not cuentas:
        print("No hay cuentas en el sistema.")
        return
    for num, datos in cuentas.items():
        print(f"Cuenta: {num} | Titular: {datos['nombre']} | Cédula: {datos['cedula']} | Saldo: {datos['saldo']:.2f} C$")

# --- R (Read): Mostrar saldo ---
def mostrar_saldo(numero_cuenta):
    print(f"\nCliente: {cuentas[numero_cuenta]['nombre']}")
    print(f"Saldo actual: {cuentas[numero_cuenta]['saldo']:.2f} C$")

# --- U (Update): Actualizar datos del perfil ---
def actualizar_cuenta(numero_cuenta):
    print("\n--- Actualizar Datos de Perfil ---")
    nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
    nueva_cedula = input("Nueva cédula (deje en blanco para no cambiar): ")
    
    if nuevo_nombre:
        cuentas[numero_cuenta]["nombre"] = nuevo_nombre
    if nueva_cedula:
        cuentas[numero_cuenta]["cedula"] = nueva_cedula
    print("Datos actualizados correctamente.")

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

# --- D (Delete): Eliminar cuenta ---
def eliminar_cuenta(numero_cuenta):
    confirmar = input("¿Está seguro de eliminar su cuenta? (S/N): ")
    if confirmar.upper() == "S":
        del cuentas[numero_cuenta]
        print("Cuenta eliminada correctamente.")
        return True
    else:
        print("Operación cancelada.")
        return False

def menu_principal():
    print("\n===== SISTEMA BANCARIO =====")
    print("1. Mostrar saldo (Read)")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Actualizar datos (Update)")
    print("5. Listar todas las cuentas (List)")
    print("6. Eliminar cuenta (Delete)")
    print("7. Cerrar sesión")
    print("8. Salir del sistema")

    return input("Seleccione una opción: ")

def main():
    while True:
        print("\n===== INICIO DE SESIÓN =====")

        numero_cuenta = input("Ingrese su número de cuenta: ")
        
        if numero_cuenta not in cuentas:
            print("Número de cuenta no encontrado.")
            continue

        cedula = input("Ingrese su cédula: ")

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
                actualizar_cuenta(numero_cuenta)
            elif opcion == "5":
                listar_cuentas()
            elif opcion == "6":
                if eliminar_cuenta(numero_cuenta):
                    break
            elif opcion == "7":
                print("Cerrando sesión...")
                break
            elif opcion == "8":
                print("Gracias por usar el sistema bancario.")
                return
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    main()