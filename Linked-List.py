class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0