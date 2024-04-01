def Recursivo(V,x,y): #Posicion inicial X y final Y
    #Caso base
    if(x==y):
        return V[x]
    #Caso General
    else:
        aux1= Recursivo(V,x,int((x+y)/2)) # division entera de la suma de x+y entonces seria (3,5,7)
        aux2= Recursivo(V,int(((x+y)/2)+1),y)
    if(aux1>aux2):
        return aux1
    else:
        return aux2
V=(3,5,7,9,11)
print(Recursivo(V,0,4))