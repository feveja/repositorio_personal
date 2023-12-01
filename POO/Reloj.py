from ParDeNumeros import ParDeNumeros

# Campos :
# horas:ParDeNumeros
# minutos:ParDeNumeros
# pantalla:str
class Reloj :

   # Constructor:crea un objeto reloj.
   # Si no recibe parametros, inicia el reloj
   # a las 00:00; si recibe, a la hora indicada
   def __init__ (self, horas = 0, minutos = 0):
      self.horas = ParDeNumeros (24)
      self.minutos = ParDeNumeros (60)
      self.setReloj (horas, minutos )


      # tic: None -> None
      # Se llama cada minuto,hace avanzar el reloj un minuto
   def tic(self):
       self.minutos.aumentar()
       if self.minutos.getValor() == 0:
           self.horas.aumentar()
       self.actualizarPantalla()


       # setReloj:int int -> None
       # efecto:Fija la hora y minuto a los especificados
   def setReloj(self, hora, minuto):
       self.horas.setValor(hora)
       self.minutos.setValor(minuto)
       self.actualizarPantalla()


       # tic: None -> None
       # getHora:None -> str
       # Devuelve la hora actual del reloj en formato HH:MM
   def getHora(self):
       return self.pantalla


       # actualizarPantalla:None -> None
       # efecto:Actualiza el string interno que lleva
       # cuenta de la hora actual
   def actualizarPantalla(self):
       self.pantalla = self.horas.toString() + ":" + self.minutos.toString ()


class TestReloj:

    def __init__(self):
        # crear un objeto con estado interesante
        self.reloj = Reloj(23, 58)


    def test(self):
        # ejercitar funcionalidad,
        # y verificar el comportamiento
        assert self.reloj.getHora() == "23:58"
        self.reloj.tic()
        assert self.reloj.getHora() == "23:59"
        self.reloj.tic()
        assert self.reloj.getHora() == "00:00"
        for i in range(60):
            self.reloj.tic()
        assert self.reloj.getHora() == "01:00"
        self.reloj.tic()
        assert self.reloj.getHora() == "01:01"

test = TestReloj()
test.test()