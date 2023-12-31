from typing import Union


class Stack:
   
    def __init__(self) -> None:
        self.stack = []
        self.rear = -1
        self.top = -1

    def __repr__(self) -> str:
        return str(self.stack)

    def __len__(self) -> int:
        return len(self.stack)

    def __delitem__(self, position: int) -> None:
        del self.stack[position]
        self.rear -= 1

    def __getitem__(self, position: int) -> Union[int, str]:
        return self.stack[position]

    def __setitem__(self, position: int, value: Union[int, str]) -> None:
        self.stack[position] = value

    def is_empty(self) -> bool:
       
        return not bool(self.stack)

    def peek(self) -> Union[int, str]:
       
        if self.is_empty():
            raise Exception("Stack Underflow. Cannot peek at an empty stack")
        return self.stack[-1]

    def pop(self) -> Union[int, str]:
       
        if self.rear == -1:
            raise Exception("Stack Underflow. Cannot pop from an empty stack")
        elif self.top == 0:
            self.rear = -1
            self.top = -1
        else:
            self.top -= 1
        return self.stack.pop()

    def push(self, val: Union[int, str]) -> None:
        
        if self.rear == -1:
            self.stack.append(val)
            self.rear = 0
            self.top = 0
        else:
            self.stack.append(val)
            self.top += 1
