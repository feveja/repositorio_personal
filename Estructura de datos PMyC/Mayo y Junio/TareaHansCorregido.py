class NodoDatoProducto:
    def __init__(self, nombre, precio, cantidad, next=None):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.next = next

    def imprimir(self):
        print("El producto:", self.nombre)
        print("El Precio:", self.precio)
        print("Cantidad en stock:", self.cantidad)


class ListaProducto:
    def __init__(self):
        self.head = None

    def agregarProductoAlFinal(self, nombre, precio, cantidad):
        nuevo_producto = NodoDatoProducto(nombre, precio, cantidad)
        if self.head is None:
            self.head = nuevo_producto
        else:
            aux = self.head
            while aux.next is not None:
                aux = aux.next
            aux.next = nuevo_producto

    def agregarProductoAlPrincipio(self, nombre, precio, cantidad):
        nuevo_producto = NodoDatoProducto(nombre, precio, cantidad)
        if self.head is None:
            self.head = nuevo_producto
        else:
            nuevo_producto.next = self.head
            self.head = nuevo_producto

    def imprimirInventario(self):
        aux = self.head
        if aux is None:
            print("No hay productos.")
        else:
            while aux is not None:
                aux.imprimir()
                aux = aux.next

    def buscarProducto(self, nombre):
        aux = self.head
        while aux is not None:
            if aux.nombre == nombre:
                aux.imprimir()
                return
            aux = aux.next
        print("El producto", nombre, "no existe en el inventario.")

    def borrarProducto(self, nombre):
        aux = self.head
        if aux is None:
            print("No hay productos en el inventario.")
            return

        if aux.nombre == nombre:
            self.head = aux.next
            print("El producto", nombre, "fue eliminado.")
            return

        prev = None
        while aux is not None and aux.nombre != nombre:
            prev = aux
            aux = aux.next

        if aux is None:
            print("El producto", nombre, "no fue encontrado.")
        else:
            prev.next = aux.next
            print("El producto", nombre, "fue eliminado.")


def menu():
    lisPro = ListaProducto()
    while True:
        print("-----MENÚ-----")
        print("1.- Agregar producto al final de la lista.")
        print("2.- Agregar producto al inicio de la lista.")
        print("3.- Imprimir inventario.")
        print("4.- Buscar producto")
        print("5.- Borrar producto")
        print("6.- Salir")

        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            lisPro.agregarProductoAlFinal(nombre, precio, cantidad)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            lisPro.agregarProductoAlPrincipio(nombre, precio, cantidad)
        elif opcion == 3:
            lisPro.imprimirInventario()
        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto a buscar: ")
            lisPro.buscarProducto(nombre)
        elif opcion == 5:
            nombre = input("Ingrese el nombre del producto a borrar: ")
            lisPro.borrarProducto(nombre)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

