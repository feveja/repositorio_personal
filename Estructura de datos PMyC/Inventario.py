class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.primer_producto = None

    def agregar_producto(self, producto):
        if not self.primer_producto:
            self.primer_producto = producto
        else:
            actual = self.primer_producto
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = producto

    def mostrar_inventario(self):
        actual = self.primer_producto
        while actual:
            print("Nombre:", actual.nombre)
            print("Precio:", actual.precio)
            print("Cantidad:", actual.cantidad)
            print("-----------------------")
            actual = actual.siguiente

    def buscar_producto(self, nombre):
        actual = self.primer_producto
        while actual:
            if actual.nombre == nombre:
                print("Producto encontrado:")
                print("Nombre:", actual.nombre)
                print("Precio:", actual.precio)
                print("Cantidad:", actual.cantidad)
                return
            actual = actual.siguiente
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        actual = self.primer_producto
        previo = None
        while actual:
            if actual.nombre == nombre:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.primer_producto = actual.siguiente
                print("Producto eliminado.")
                return
            previo = actual
            actual = actual.siguiente
        print("Producto no encontrado.")

# Crear instancia de inventario
inventario = Inventario()

# Agregar productos
inventario.agregar_producto(Producto("Laptop", 800, 5))
inventario.agregar_producto(Producto("Teléfono", 400, 10))
inventario.agregar_producto(Producto("Tablet", 300, 8))

# Mostrar inventario
print("Inventario de productos:")
inventario.mostrar_inventario()

# Buscar producto
print("Buscando producto:")
inventario.buscar_producto("Teléfono")

# Eliminar producto
print("Eliminando producto:")
inventario.eliminar_producto("Tablet")

# Mostrar inventario actualizado
print("Inventario después de eliminar:")
inventario.mostrar_inventario()
