class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self)

    def __add__(self, node, elem):
        if elem.data < node.data:
            if node.left is None:
                node.left = elem
            else:
                self.__add__(node.left, elem)
        else:
            if node.right is None:
                node.right = elem
            else:
                self.__add__(node.right, elem)

    def add_element(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__add__(self.root, Node(data))

    def remove_element(self, data):
        current_node = self.head
        while current_node != self.tail:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next

    def __search__(self, node, data):
        if node.data == data:
            return True
        elif node.data < data:
            if node.right is None:
                return False
            else:
                self.__search__(node.right, data)
        else:
            if node.left is None:
                return False
            else:
                self.__search__(node.left, data)

    def search_element(self, data):
        if self.root.data == data:
            return True
        else:
            self.__search__(self.root, data)

    def __str__(self):
        array = []
        current_node = self.head
        while current_node:
            array.append(str(current_node.data))
            current_node = current_node.next
        return "[" + "->".join(array) + "]"