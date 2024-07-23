import numpy as np
#sumaArra(a,b): list list -> list
#Entrega un nuevo arreglo con el resultado de la suma de a y b
def sumaArr(a,b):
    anum=str()
    for i in range(len(a)):
        anum += str(a[i])
    bnum=str()
    for i in range(len(b)):
        bnum += str(b[i])
    anum = int(anum)
    bnum = int(bnum)
    cnum = anum+bnum
    
    cnum = str(cnum)

    c = np.zeros(len(cnum))
    for i in range(len(c)):
        c[i] = cnum[i]
    return c

x = []
y = []
while True:
    x1 = input("Inserte una elemento a la lista 1: ")
    if x1 != "x":
        x.append(x1)
    else:
        break
while True:
    y1 = input("Inserte un elemento a la lista 2: ")
    if y1 != "x":
        y.append(y1)
    else:
        break

print(sumaArr(x,y))