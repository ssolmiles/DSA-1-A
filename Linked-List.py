class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self._length += 1
    return self


def prepend(self, data):
    new_node = Node(data)
    if not self._length:
        self.head = self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
    self._length += 1
    return self


#linked list'
#double linked list