from __future__ import annotations
from typing import Any, Iterator, Optional
 
#building blocks
class Node:
    __slots__ = ("value", "prev", "next")
 
    def __init__(self, value: Any):
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None