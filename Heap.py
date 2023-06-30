from typing import Union

def get_parent_position(position: int) -> int:
    return (position - 1) // 2
def get_left_child_position(position: int) -> int:
    return (2 * position) + 1
def get_right_child_position(position: int) -> int:
    return (2 * position) + 2
class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def extract_min(self) -> Union[int, str]:
        if self.elements == 0:
            raise RuntimeError("Heap Underflow. Cannot extract min from a empty heap")

        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem = self.heap.pop()
        self.elements -= 1
        if self.elements > 0:
            self._bubble_down(0)
        return elem

    def insert(self, elem: Union[int, str]) -> None:
        self.heap.append(elem)
        self._bubble_up(self.elements)
        self.elements += 1
    def peek_min(self) -> Union[int, str]:
        if self.elements == 0:
            raise RuntimeError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, curr_pos: int) -> None:
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        elem = self.heap[curr_pos]
        parent = self.heap[parent_position]
        if parent > elem:
            self._swap_nodes(parent_position, curr_pos)
            self._bubble_up(parent_position)

    def _bubble_down(self, curr_pos: int) -> None:
        elem = self.heap[curr_pos]
        child_left_position = get_left_child_position(curr_pos)
        child_right_position = get_right_child_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            child_left = self.heap[child_left_position]
            child_right = self.heap[child_right_position]
            if child_right < child_left:
                if child_right < elem:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(child_right_position)
        if child_left_position < self.elements:
            child_left = self.heap[child_left_position]
            if child_left < elem:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(child_left_position)
        else:
            return
        if child_right_position < self.elements:
            child_right = self.heap[child_right_position]
            if child_right < elem:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(child_right_position)

    def _swap_nodes(self, pos1: int, pos2: int) -> None:
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]


class MaxHeap:
   
    def __init__(self) -> None:
        self.heap = []
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def extract_max(self) -> Union[int, str]:
        
        if self.elements == 0:
            raise RuntimeError("Heap Underflow. Cannot extract max from a empty heap")

        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem = self.heap.pop()
        self.elements -= 1
        if self.elements > 0:
            self._bubble_down(0)
        return elem

    def insert(self, elem: Union[int, str]) -> None:
        
        self.heap.append(elem)
        self._bubble_up(self.elements)
        self.elements += 1

    def peek_max(self) -> Union[int, str]:
        
        if self.elements == 0:
            raise RuntimeError("Heap is empty")
        return self.heap[0]

    def _bubble_up(self, curr_pos: int) -> None:
       
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        elem = self.heap[curr_pos]
        parent = self.heap[parent_position]
        if parent < elem:
            self._swap_nodes(parent_position, curr_pos)
            self._bubble_up(parent_position)

    def _bubble_down(self, curr_pos: int) -> None:
        
        elem = self.heap[curr_pos]
        child_left_position = get_left_child_position(curr_pos)
        child_right_position = get_right_child_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            child_left = self.heap[child_left_position]
            child_right = self.heap[child_right_position]
            if child_right > child_left:
                if child_right > elem:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(child_right_position)
        if child_left_position < self.elements:
            child_left = self.heap[child_left_position]
            if child_left > elem:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(child_left_position)
        else:
            return
        if child_right_position < self.elements:
            child_right = self.heap[child_right_position]
            if child_right > elem:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(child_right_position)

    def _swap_nodes(self, pos1: int, pos2: int) -> None:
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
