
class NodoDatoProducto:
  def __init__(self,nombre,precio,cantidad,next):
    self.nombre=nombre
    self.precio=precio
    self.cantiad=cantidad
    self.next=next

  def imprimir(self):
    print("El producto: ",self.nombre)
    print("El Precio: ",self.precio)
    print("Cantidad en stock: ",self.cantidad)

class NodoDatoDobleProducto:
  def __init__(self,prev,nombre,precio,cantidad,next):
    self.prev=prev
    self.nombre=nombre
    self.precio=precio
    self.cantidad=cantidad
    self.next=next

  def imprimirDoble(self):
    print("El Producto: ", self.nombre)
    print("El Precio: ",self.precio)
    print("Cantidad en Stock: ",self.cantidad)

class ListaProducto:
  def __init__(self):
    self.head=None

  def agregarProductoAlFinal(self,nombre,precio,cantidad):
    aux=self.head
    if aux==None:
      self.head=NodoDatoProducto(nombre,precio,cantidad,None)
    else:
      while aux.next!=None:
        aux=aux.next
      aux.next=NodoDatoProducto(nombre,precio,cantidad,None)

  def agregarProductoAlPrincipio(self,nombre,precio,cantidad):
    aux=NodoDatoProducto(nombre,cantidad,precio,None)
    if self.head==None:
      self.head=aux
    else:
      aux.next=self.head
      self.head=aux

  def imprimirInventario(self):
    aux=self.head
    if aux==None:
      print("No hay productos.")
    else:
      while aux.next!=None:
        print("El producto:", aux.nombre)
        print("Hay la cantidad de: ", aux.cantidad)
        aux=aux.next

  def buscarProducto(self,nombre):
    aux=self.head
    if aux==None:
      print("no hay predutos en el inventario.")
    else:
      while aux.next!=None:
        if aux.nombre==nombre:
          aux.imprimir()
          return
        else:
          aux=aux.next
      print("El producto ",nombre," no esxiste en el inventario.")

  def borrarProducto(self,nombre):
    aux=self.head
    if aux==None:
      print("No hay Productos en el inventario.")
    else:
      cont=0
      while aux.next!=None:
        if aux.nombre==nombre:
          aux=aux.next
          cont=1
        else:
          aux.imprimir()
          aux=aux.next

      if cont==0:
        print("El Producto ",nombre," no fue enconrado.")
      else:
        print("El Producto ",nombre," fue eliminado")

class ListaDobleProducto:
  def __init__(self):
    self.head=Nodo(None,"0","0","0",None)
    self.head.prev=self.head
    self.head.next=self.head

print("-----MENÚ-----")
print("1.- Agregar produto al final de la lista.")
print("2.- Agregar producto al inicio de la lista.")
print("3.- Imprimir inventario.")
print("4.- Buscar prodructo")
print("5.- Borrar Prdoducto")
print("6.- Salir")
lisPro=ListaProducto()
opcion=int(input("ingrese la opción:"))

while opcion==1 or opcion==2 or opcion==3 or opcion==4 or opcion==5:
  if opcion==1:
    nom=str(input("ingrese nombre del producto"))
    pre=int(input("ingrese Precio del producto"))
    can=int(input("ingrese cantidad de produto"))
    lisPro.agregarProductoAlFinal(nom,pre,can)

  if opcion==2:
    nom=str(input("ingrese nombre del producto"))
    pre=int(input("ingrese Precio del producto"))
    can=int(input("ingrece cantidad de producto"))
    lisPro.agregarProductoAlPrincipio(nom,pre,can)

  if opcion==3:
    lisPro.imprimirInventario()

  if opcion==4:
    nom=str(input("ingrese el nombre del producto a buscar"))
    lisPro.buscarProducto(nom)

  if opcion==5:
    nom=str(input("ingrese el nombre del producto a borrar"))
    lisPro.borrarProducto(nom)

  else:
    break