class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, valor):
        if not self.head:
            self.head = Node(valor)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(valor)



    def swap(self, n1, n2):
        if n1 == n2:
            return

        # Punteros iniciales
        prev_n1 = prev_n2 = None
        node1 = node2 = self.head

        # Encontrar n1 y su anterior
        while node1 and node1.valor != n1:
            prev_n1 = node1
            node1 = node1.next

        # Encontrar n2 y su anterior
        while node2 and node2.valor != n2:
            prev_n2 = node2
            node2 = node2.next

        if not node1 or not node2:
            return  # Uno o ambos nodos no están en la lista

        # Intercambio
        if prev_n1:
            prev_n1.next = node2
        else:
            self.head = node2

        if prev_n2:
            prev_n2.next = node1
        else:
            self.head = node1

        node1.next, node2.next = node2.next, node1.next
