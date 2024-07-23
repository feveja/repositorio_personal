class HistoryNode:
    def __init__(self, url):
        self.url = url
        self.next = None

class BrowserHistory:
    def __init__(self):
        self.head = None

    def visit(self, url):
        """
        Añade una nueva URL al final del historial.
        """
        new_node = HistoryNode(url)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_history(self, url):
        """
        Elimina una URL específica del historial.
        """
        temp = self.head

        if temp is not None:
            if temp.url == url:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.url == url:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def find_url(self, url):
        """
        Busca una URL específica en el historial.
        """
        current = self.head
        while current is not None:
            if current.url == url:
                return True
            current = current.next
        return False

    def display_history(self):
        """
        Muestra todas las URLs en el historial en el orden en que fueron visitadas.
        """
        history = []
        current_node = self.head
        while current_node is not None:
            history.append(current_node.url)
            current_node = current_node.next
        print(history)

# Uso del sistema de historial de navegación
history = BrowserHistory()
history.visit("http://example.com")
history.visit("http://example.org")
history.visit("http://example.net")
history.display_history()  # Output: ["http://example.com", "http://example.org", "http://example.net"]
print(history.find_url("http://example.org"))  # Output: True
history.delete_history("http://example.org")
history.display_history()  # Output: ["http://example.com", "http://example.net"]
print(history.find_url("http://example.org"))  # Output: False
