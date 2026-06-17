class Cuenta:
    def __init__(self, numero_cuenta, nombre, cedula, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "saldo": self.saldo
        }

    @staticmethod
    def from_dict(numero_cuenta, data):
        return Cuenta(
            numero_cuenta,
            data["nombre"],
            data["cedula"],
            data["saldo"]
        )