class NodoProducto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.siguiente = None

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)
        print()


class ListaProducto:
    def __init__(self):
        self.primer_producto = None

    def agrega_al_final(self, nombre, precio, cantidad):
        nuevo_producto = NodoProducto(nombre, precio, cantidad)
        if self.primer_producto is None:
            self.primer_producto = nuevo_producto
            return
        actual = self.primer_producto
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_producto

    def agrega_al_principio(self, nombre, precio, cantidad):
        nuevo_producto = NodoProducto(nombre, precio, cantidad)
        nuevo_producto.siguiente = self.primer_producto
        self.primer_producto = nuevo_producto

    def mostrar_inventario(self):
        actual = self.primer_producto
        while actual:
            actual.imprimir()
            actual = actual.siguiente

    def buscar_producto(self, nombre_producto):
        actual = self.primer_producto
        while actual:
            if actual.nombre == nombre_producto:
                print("Producto encontrado:")
                actual.imprimir()
                return
            actual = actual.siguiente
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre_producto):
        actual = self.primer_producto
        previo = None
        while actual:
            if actual.nombre == nombre_producto:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.primer_producto = actual.siguiente
                print("Producto eliminado:", nombre_producto)
                return
            previo = actual
            actual = actual.siguiente
        print("Producto no encontrado.")


# Ejemplo de uso:
lista_productos = ListaProducto()

# Agregar productos
lista_productos.agrega_al_final("Laptop", 500, 3)
lista_productos.agrega_al_final("Teléfono", 200, 5)
lista_productos.agrega_al_principio("Tablet", 300, 2)

# Mostrar inventario
print("Inventario:")
lista_productos.mostrar_inventario()

# Buscar producto
lista_productos.buscar_producto("Laptop")
lista_productos.buscar_producto("Smartwatch")

# Eliminar producto
lista_productos.eliminar_producto("Tablet")
lista_productos.eliminar_producto("Smartphone")

# Mostrar inventario después de eliminar
print("Inventario después de eliminar:")
lista_productos.mostrar_inventario()
lista_productos = ListaProducto()
