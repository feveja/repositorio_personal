class ReservationNode:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.next = None

class ReservationList:
    def __init__(self):
        self.head = None

    def add_reservation(self, name, time):
        """
        Añade una nueva reserva al final de la lista.
        """
        new_node = ReservationNode(name, time)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def cancel_reservation(self, name):
        """
        Elimina una reserva específica de la lista usando el nombre de la persona.
        """
        temp = self.head

        if temp is not None:
            if temp.name == name:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.name == name:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def find_reservation(self, name):
        """
        Busca una reserva específica en la lista.
        """
        current = self.head
        while current is not None:
            if current.name == name:
                return True
            current = current.next
        return False

    def display_reservations(self):
        """
        Muestra todas las reservas en el orden en que fueron realizadas.
        """
        reservations = []
        current_node = self.head
        while current_node is not None:
            reservations.append((current_node.name, current_node.time))
            current_node = current_node.next
        print(reservations)

# Uso del sistema de gestión de reservas
reservations = ReservationList()
reservations.add_reservation("Alice", "19:00")
reservations.add_reservation("Bob", "20:00")
reservations.add_reservation("Charlie", "21:00")
reservations.display_reservations()  # Output: [("Alice", "19:00"), ("Bob", "20:00"), ("Charlie", "21:00")]
print(reservations.find_reservation("Bob"))  # Output: True
reservations.cancel_reservation("Bob")
reservations.display_reservations()  # Output: [("Alice", "19:00"), ("Charlie", "21:00")]
print(reservations.find_reservation("Bob"))  # Output: False
