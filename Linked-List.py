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