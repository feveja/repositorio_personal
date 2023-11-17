class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        contacto = {"Nombre": nombre, "Teléfono": telefono}
        self.contactos.append(contacto)
        print(f"Contacto {nombre} agregado a la agenda.")

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['Nombre'] == nombre:
                print(f"Contacto encontrado - Nombre: {contacto['Nombre']}, Teléfono: {contacto['Teléfono']}")
                return
        print(f"Contacto con el nombre {nombre} no encontrado.")

# Ejemplo de uso:
agenda = Agenda()
agenda.agregar_contacto("Ana", "123456789")
agenda.agregar_contacto("Carlos", "987654321")
agenda.mostrar_contactos()
agenda.buscar_contacto("Ana")
