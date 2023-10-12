#def sobreviviente(n,m):
#    personas = list()
#    for i in range(n):
#        personas.append(i+1)
#    print(personas)
#    indice = 0 
#    while len(personas)>1:
#        indice = (indice + m) % len(personas)
#        personas.pop(indice)
#        
#    return personas

def sobreviviente(n,m):
    personas = list()
    for i in range(n):
        personas.append(i+1)
    print(personas)
    if n%2 == 0:
        indice = 1
    else:
        indice = 0
    #Caso par
    while len(personas)>1:
        indice = (indice + m)-1
        if indice >= len(personas):
            indice = abs(indice - len(personas))
            personas.pop(indice)
        else:
            personas.pop(indice)
    return personas

print(sobreviviente(13,1))
print(sobreviviente(12,2))
print(sobreviviente(15,1))