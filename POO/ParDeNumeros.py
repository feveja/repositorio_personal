# Campos:
# limite: int
# valor: int
class ParDeNumeros :
   # Constructor: crea un objeto que almacena
   # dos números y se reinicia
   # a cero cuando se sobrepasa el limite
   def __init__ (self,limite):
       self.limite = limite
       self.valor = 0
       
       
   # getValor: None -> int
   # Retorna el valor actual
   def getValor ( self ):
      return self.valor


   # setValor: int -> None
   # efecto: Reemplaza el valor del par por nuevo valor
   def setValor(self, nuevoValor):
       if (nuevoValor >= 0) and (nuevoValor < self.limite):
           self.valor = nuevoValor


   # toString: -> str
   # Retorna el valor almacenado en un string que
   # contiene los numeros del par; si el valor es menor
   # que diez, se le debe anteponer un cero
   def toString(self):
       if self.valor < 10:
           return "0" + str(self.valor)
       else:
           return str(self.valor)


   # aumentar: None -> None
   # efecto: Aumenta en una unidad el valor almacenado
   # en el par,
   # reiniciando a cero si se sobrepasa el limite
   def aumentar(self):
       self.valor = (self.valor + 1) % self.limite


# Para simplificar la implementacion de los tests,
# este codigo se incluye en el archivo donde se
# encuentra la definicion de la clase ParDeNumeros


class TestParDeNumeros:

    def __init__(self):
        # crear un objeto con estado interesante
        self.par = ParDeNumeros(3)

    def test(self):
        # ejercitar funcionalidad
        # y verificar el comportamiento
        assert self.par.getValor() == 0
        self.par.aumentar()
        assert self.par.getValor() == 1
        self.par.aumentar()
        assert self.par.getValor() == 2
        self.par.aumentar()
        assert self.par.getValor() == 0
        self.par.aumentar()
        assert self.par.getValor() == "01" #Da AssertionError

# ejecucion del test
test = TestParDeNumeros()
test.test()