#feliperodrigo.vera@alumnos.ulagos.cl
#potencia: int int -> int
#Obj:calcula la potencia de una base y exponente
#ejemplo: potencia(2,3) = 8
#Ayuda Caso base exponente == 0
#Ayuda Caso Recursiv
def potencia(base,exponente):
    if exponente == 0: #Caso base
        return 1
    else:
        return base*potencia(base,exponente-1) #Caso Recursivo 

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

print(potencia(base,exponente))
