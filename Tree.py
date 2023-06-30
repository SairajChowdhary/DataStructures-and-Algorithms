from __future__ import annotations
from typing import Any, Optional, Union


class Node:
    def __init__(
        self, val: int, left: Optional[Node] = None, right: Optional[Node] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: Any) -> bool:
        if type(other) == Node and self.val == other.val:
            return self.left == other.left and self.right == other.right
        return False

    def __repr__(self) -> str:
        return self.to_str()

    def height_helper(self) -> int:
      
        left_height, right_height = 0, 0
        if self.left is not None:
            left_height = self.left.height_helper()
        if self.right is not None:
            right_height = self.right.height_helper()
        return max(left_height, right_height) + 1

    def insert_helper(self, val: int) -> None:
        
        if self.val > val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert_helper(val)
        elif self.val < val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert_helper(val)

    def num_nodes_helper(self) -> int:
       
        left, right = 0, 0
        if self.left:
            left = self.left.num_nodes_helper()
        if self.right:
            right = self.right.num_nodes_helper()
        return left + right + 1

    def to_str(self) -> str:
       
        if self.right is None and self.left is None:
            return f"('{self.val}')"
        elif self.left is not None and self.right is None:
            return f"({self.left.to_str()}, '{self.val}', null)"
        elif self.left is None and self.right is not None:
            return f"(null, '{self.val}', {self.right.to_str()})"
        elif self.left is not None and self.right is not None:
            return f"({self.left.to_str()}, '{self.val}', {self.right.to_str()})"


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def __eq__(self, other: Any) -> bool:
        if type(other) == BinaryTree:
            return self.root == other.root
        return False

    def __len__(self) -> int:
        if self.root:
            return self.root.num_nodes_helper()
        return 0

    def __repr__(self) -> str:
        return str(self.root)

    def find_height(self) -> int:
        
        if self.root:
            return self.root.height_helper()
        return 0


class BinarySearchTree(BinaryTree):
   

    def __init__(self) -> None:
        BinaryTree.__init__(self)

    def add(self, val: Union[int, str]) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self.root.insert_helper(val)
