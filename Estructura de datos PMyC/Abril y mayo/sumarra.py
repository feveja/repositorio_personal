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

x = [9,8,7,6]
y = [8,7,6,5]
print(sumaArr(x,y))

    