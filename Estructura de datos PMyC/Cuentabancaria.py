#CuentaBancaria:
#Atributos: titular, saldo
#Metodos: depositar, retirar, consultar_saldo
#Crear una instancia d-e la clase CuentaBancaria,Deposite,Retire,Consultesaldo
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    #depositar: int -> str
    #Obj: deposita la cantidad indicada en el saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
    #retirar: int -> str
    #Obj: retira la cantidad indicada en el saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self.saldo}"
        else:
            return "Fondos insuficientes."
    #consultar_saldo: -> str
    #Obj: muestra el saldo
    def consultar_saldo(self):
        return f"Saldo disponible: ${self.saldo}"

# Crear una instancia de la clase CuentaBancaria
mi_cuenta = CuentaBancaria("Juan")

# Depositar dinero
print(mi_cuenta.depositar(100))  # Imprime "Depósito de $100 realizado. Nuevo saldo: $100"

# Retirar dinero
print(mi_cuenta.retirar(50))     # Imprime "Retiro de $50 realizado. Nuevo saldo: $50"
print(mi_cuenta.retirar(80))     # Imprime "Fondos insuficientes."

# Consultar saldo
print(mi_cuenta.consultar_saldo())  # Imprime "Saldo disponible: $50"
