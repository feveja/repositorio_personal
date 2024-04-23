#Libro: 
#atributos: titulo, autor, genero, precio
#metodos: mostrar_info
#crear instancia de la clase
class Libro:

    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Género: {self.genero}")
        print(f"Precio: ${self.precio}")

# Crear instancias de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 20)
libro2 = Libro("El Alquimista", "Paulo Coelho", "Ficción", 15)

# Mostrar información de los libros
libro1.mostrar_info()
print("-------------------")
libro2.mostrar_info()
