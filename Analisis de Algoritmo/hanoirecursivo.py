def recursivo(n,origen,auxiliar,destino):
    if n==1:
        print("Mover disco de ",origen," a ",destino)
    else:
        recursivo(n-1,origen,destino,auxiliar)
        print("Mover disco de ",origen," a ",destino)
        recursivo(n-1,auxiliar,origen,destino)

recursivo(4,"Origen","Auxiliar","Destino")
