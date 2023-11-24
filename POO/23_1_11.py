# Clase Cuenta
# numero : str
# saldo : int

class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = str(numero)
        self.saldo = int(saldo)

    # Imprime el saldo actual de la cuenta
    def getsaldo(self):
        return self.saldo

    # Imprime el numero de cuenta
    def getnumero(self):
        return self.numero

    # Imprime el numero de cuenta y su saldo actual
    def __str__(self):
        return f"cuenta={self.numero},saldo={self.saldo}"

    # Compara el saldo actual con el saldo actual de otra cuenta
    def compareTo(self, otra_cuenta):
        return self.saldo - otra_cuenta.saldo

    # El saldo actual es aumentado por el monto ingresado
    def depositar(self, monto):
        self.saldo += monto

    # El saldo actual es reducido por el monto ingresado, evitando que el saldo actual sea > 0
    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False


# Clase Cuenta1(Cuenta)
# Hereda todos los atributos de la clase madre
class Cuenta1(Cuenta):
    # El saldo actual es reducido por el monto ingresado, sin restricciones
    def girar(self, monto):
        self.saldo -= monto
        
c= Cuenta("1",100)
assert c.getnumero()=="1"
assert c.getsaldo()==100
B = Cuenta1("1",200)
B.girar(300)
assert B.getsaldo()== -100