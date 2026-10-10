from __future__ import annotations
from typing import Any, Iterator, Optional
 
#building blocks
class Node:
    __slots__ = ("value", "prev", "next")
 
    def __init__(self, value: Any):
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class DoublyLinkedList:
    """Reusable DLL with head/tail pointers and O(1) node removal."""
 
    def __init__(self, items=()):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0
        for item in items:
            self.append(item)
 
    def __len__(self) -> int:
        return self._size
 
    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next
 
    def __reversed__(self) -> Iterator[Any]:
        cur = self.tail
        while cur:
            yield cur.value
            cur = cur.prev
 
    def __repr__(self) -> str:
        return " <-> ".join(map(repr, self)) or "(empty)"
 
    def append(self, value) -> Node:
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev, self.tail.next = self.tail, node
            self.tail = node
        self._size += 1
        return node
 
    def appendleft(self, value) -> Node:
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next, self.head.prev = self.head, node
            self.head = node
        self._size += 1
        return node
 
    def insert_after(self, node: Node, value) -> Node:
        new = Node(value)
        new.prev, new.next = node, node.next
        if node.next:
            node.next.prev = new
        else:
            self.tail = new
        node.next = new
        self._size += 1
        return new
 
    def insert_before(self, node: Node, value) -> Node:
        if node.prev is None:
            return self.appendleft(value)
        return self.insert_after(node.prev, value)
 
    def remove_node(self, node: Node) -> Any:
        """O(1) removal - the main advantage over a singly linked list."""
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None
        self._size -= 1
        return node.value
 
    def pop(self) -> Any:
        if not self.tail:
            raise IndexError("pop from empty list")
        return self.remove_node(self.tail)
 
    def popleft(self) -> Any:
        if not self.head:
            raise IndexError("popleft from empty list")
        return self.remove_node(self.head)
 
    def move_to_front(self, node: Node) -> None:
        if node is self.head:
            return
        value = self.remove_node(node)
        node.value = value
        node.next, node.prev = self.head, None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1
 
    def find(self, value) -> Optional[Node]:
        cur = self.head
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None
 
    def reverse(self) -> None:
        cur = self.head
        while cur:
            cur.prev, cur.next = cur.next, cur.prev
            cur = cur.prev
        self.head, self.tail = self.tail, self.head
 
 
def title(n: int, text: str) -> None:
    print(f"\n{'=' * 60}\nSample {n}: {text}\n{'=' * 60}")

def sample_01_basic_operations():
    title(1, "Basic operations")
    dll = DoublyLinkedList([10, 20, 30])
    dll.appendleft(5)
    node_20 = dll.find(20)
    dll.insert_after(node_20, 25)
    print("List:", dll)
    print("Reversed iteration:", list(reversed(dll)))
    dll.remove_node(node_20)
    print("After removing 20:", dll, "| size =", len(dll))
    dll.reverse()
    print("After reverse():", dll)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: dict[Any, Node] = {}
        self.order = DoublyLinkedList()  # head = most recent, tail = least recent
 
    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return None
        self.order.move_to_front(node)
        return node.value[1]
 
    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = (key, value)
            self.order.move_to_front(node)
            return
        if len(self.order) >= self.capacity:
            old_key, _ = self.order.pop()
            del self.map[old_key]
        self.map[key] = self.order.appendleft((key, value))

class Node: 
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self._length = 1  

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    
 