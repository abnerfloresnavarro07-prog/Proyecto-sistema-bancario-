class Cuenta:
    def __init__(self, numero_cuenta, nombre, cedula, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo


    def to_dict(self):
        """Convierte el objeto en diccionario para guardarlo en JSON"""
        return {
            "numero_cuenta": self.numero_cuenta,
            "nombre": self.nombre,
            "cedula": self.cedula,
            "saldo": self.saldo
        }


    @staticmethod
    def from_dict(data):
        """Convierte JSON a objeto Cuenta"""
        return Cuenta(
            data["numero_cuenta"],
            data["nombre"],
            data["cedula"],
            data.get("saldo", 0.0)
        )