class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Crear un objeto cuadrado
mi_cuadrado = Cuadrado(5)

# Acceder a los métodos
area = mi_cuadrado.calcular_area()
perimetro = mi_cuadrado.calcular_perimetro()

# Imprimir resultados
print(f"Área del cuadrado: {area}")
print(f"Perímetro del cuadrado: {perimetro}")
