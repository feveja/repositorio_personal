def mochila_01(objetos, capacidad_mochila):
    objetos_ordenados = sorted(objetos, key=lambda x: x[1]/x[0], reverse=True)
    mochila = [0] * len(objetos)
    beneficio_total = 0

    for i in range(len(objetos_ordenados)):
        peso_objeto, beneficio_objeto = objetos_ordenados[i]
        if capacidad_mochila >= peso_objeto:
            mochila[i] = 1
            capacidad_mochila -= peso_objeto
            beneficio_total += beneficio_objeto

    return mochila, beneficio_total

# Ejemplo de uso
objetos = [(2, 40), (5, 30), (10, 50), (5, 10), (3, 60)]
capacidad_mochila = 16
mochila, beneficio = mochila_01(objetos, capacidad_mochila)
print("Objetos seleccionados:", mochila)
print("Beneficio total:", beneficio)