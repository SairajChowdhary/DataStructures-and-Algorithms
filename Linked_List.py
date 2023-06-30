from typing import Iterable


class Node:
    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        if self.next:
            return f"{str(self.val)} => {str(self.next)}"
        return str(self.val)


class LinkedList:
   
 def __init__(self) -> None:
        self.head = None
        self.rear = None
        self.length = 0

    def __repr__(self) -> str:
        return str(self.head)

    def add(self, val: int = 0):
        self.length += 1
        if self.head is None:
            self.head = Node(val)
            self.rear = self.head
        else:
            self.rear.next = Node(val)
            self.rear = self.rear.next

    def __len__(self) -> int:
        return self.length
 def __iter__(self) -> Iterable:
        self.curr = self.head
        return self

def __next__(self) -> int:
        if self.curr:
            value = self.curr.val
            self.curr = self.curr.next
            return value
        else:
            raise StopIteration
