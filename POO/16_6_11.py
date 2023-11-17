class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def obtener_saldo(self):
        return self.saldo

# Ejemplo de uso de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Juan Perez", 1000)
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
saldo_actual = mi_cuenta.obtener_saldo()

print(f"Titular de la cuenta: {mi_cuenta.titular}")
print(f"Saldo actual de la cuenta: {saldo_actual}")