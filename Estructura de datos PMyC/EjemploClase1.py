#Una clase es como un plano para crear objetos. 
#Define las propiedades y el comportamiento de esos objetos 
class Persona:
    #El constructor es un método especial en Python que se llama automáticamente cuando
    # se crea una instancia de la clase. Se utiliza para inicializar los atributos del objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Las funciones en una clase se llaman métodos.
    #Estos métodos pueden realizar acciones relacionadas con los objetos de esa clase
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Crear instancias de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Acceder a los atributos y métodos de las instancias
print(persona1.nombre)  # Imprime "Juan"
print(persona2.edad)    # Imprime 25
print(persona1.saludar())  # Imprime "Hola, soy Juan y tengo 30 años."
print(persona2.saludar())  # Imprime "Hola, soy María y tengo 25 años."
