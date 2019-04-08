from utilities.Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return str(self)

    def add_element(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node

    def remove_element(self, data):
        current_node = self.head
        while current_node != self.tail:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next

    def search_element(self, data):
        current_node = self.head
        while current_node != self.tail:
            if current_node.data == data:
                return True
            current_node = current_node.next

        return False

    def __str__(self):
        array = []
        current_node = self.head
        while current_node:
            array.append(str(current_node.data))
            current_node = current_node.next
        return "[" + "->".join(array) + "]"
