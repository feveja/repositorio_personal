class Conjunto:
    def __init__(self, elementos=[]):
        self.elementos = set(elementos)

    def cardinal(self):
        return len(self.elementos)

    def union(self, otro_conjunto):
        nuevo_conjunto = Conjunto(list(self.elementos.union(otro_conjunto.elementos)))
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        nuevo_conjunto = Conjunto(list(self.elementos.intersection(otro_conjunto.elementos)))
        return nuevo_conjunto

    def complemento(self, conjunto_universo):
        nuevo_conjunto = Conjunto(list(conjunto_universo.elementos.difference(self.elementos)))
        return nuevo_conjunto

# Ejemplo de uso:
conjunto1 = Conjunto([1, 2, 3, 4, 5])
conjunto2 = Conjunto([4, 5, 6, 7, 8])

print("Conjunto 1:", conjunto1.elementos)
print("Conjunto 2:", conjunto2.elementos)

print("Cardinal de conjunto 1:", conjunto1.cardinal())
print("Cardinal de conjunto 2:", conjunto2.cardinal())

union_resultado = conjunto1.union(conjunto2)
print("Unión de conjunto 1 y conjunto 2:", union_resultado.elementos)

interseccion_resultado = conjunto1.interseccion(conjunto2)
print("Intersección de conjunto 1 y conjunto 2:", interseccion_resultado.elementos)

conjunto_universo = Conjunto([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
complemento_resultado = conjunto1.complemento(conjunto_universo)
print("Complemento de conjunto 1 en el conjunto universo:", complemento_resultado.elementos)
