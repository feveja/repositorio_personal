import numpy as np
def sumaArr(a,b):
    # Inicialización de una cadena vacía para almacenar el número formado por los elementos de 'a'
    anum = str()
    # Iteración sobre los elementos de 'a'
    for i in range(len(a)):
        # Concatenación de cada elemento de 'a' convertido a cadena
        anum += str(a[i])
    
    # Inicialización de una cadena vacía para almacenar el número formado por los elementos de 'b'
    bnum = str()
    # Iteración sobre los elementos de 'b'
    for i in range(len(b)):
        # Concatenación de cada elemento de 'b' convertido a cadena
        bnum += str(b[i])
    
    # Conversión de las cadenas de números a enteros
    anum = int(anum)
    bnum = int(bnum)
    
    # Suma de los números enteros obtenidos de 'a' y 'b'
    cnum = anum + bnum
    
    # Conversión del resultado de la suma nuevamente a cadena
    cnum = str(cnum)

    # Inicialización de un arreglo de numpy de ceros con la misma longitud que la cadena 'cnum'
    c = np.zeros(len(cnum), dtype=int)
    # Iteración sobre los caracteres de la cadena 'cnum'
    for i in range(len(c)):
        # Asignación de cada caracter convertido a entero al arreglo 'c'
        c[i] = cnum[i]
    # Retorno del arreglo 'c'
    return c

# Definición de dos listas de números
x = [9,8,7,6]
y = [8,7,6,5]

# Llamada a la función 'sumaArr' pasando las listas 'x' y 'y' como argumentos
print(sumaArr(x,y))  
