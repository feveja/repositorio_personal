# Búsqueda binaria, versión recursiva
# busca x en el arreglo a, retorna subíndice o -1 si no está
def bbin(x,a):

    # puntapié inicial
    n=len(a)

    # vamos a utilizar una función auxiliar, que se define fuera de 
    # esta función bbin
    return bbin_rec(x,a,0,n-1)

# Definimos una función auxiliar para
# buscar en el subarreglo a[i],...,a[j]
def bbin_rec(x,a,i,j):
    if i>j:
        return -1
    k=(i+j)//2
    if x==a[k]:
        return k
    if x<a[k]:
        return bbin_rec(x,a,i,k-1)
    else:
        return bbin_rec(x,a,k+1,j)