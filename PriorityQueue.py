def get_parent_position(position: int) -> int:
      return (position - 1) // 2


def get_child_left_position(position: int) -> int:
  return (2 * position) + 1


def get_child_right_position(position: int) -> int:
    return (2 * position) + 2


class MinPriorityQueue:
   
 def __init__(self) -> None:
        self.heap = []
        self.position_map = {}
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def __contains__(self, key: int) -> bool:
        return key in self.position_map

    def is_empty(self) -> bool:
        return self.elements == 0

    def push(self, elem: int, weight: int) -> None:
       
        self.heap.append((elem, weight))
        self.position_map[elem] = self.elements
        self.elements += 1
        self._bubble_up(elem)

    def peek_min(self):
        if self.elements == 0:
            raise RuntimeError("Queue is empty")
        elem, _ = self.heap[0]
        return elem

    def extract_min(self) -> int:
      
        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem, _ = self.heap.pop()
        del self.position_map[elem]
        self.elements -= 1
        if self.elements > 0:
            bubble_down_elem, _ = self.heap[0]
            self._bubble_down(bubble_down_elem)
        return elem

    def get_priority(self, key: int) -> int:
        if key not in self:
            raise ValueError(f"{key} not found")
        _, weight = self.heap[self.position_map[key]]
        return weight

    def update_key(self, elem: int, weight: int) -> None:
       
        position = self.position_map[elem]
        self.heap[position] = (elem, weight)
        if position > 0:
            parent_position = get_parent_position(position)
            _, parent_weight = self.heap[parent_position]
            if parent_weight > weight:
                self._bubble_up(elem)
            else:
                self._bubble_down(elem)
        else:
            self._bubble_down(elem)

    def _bubble_up(self, elem: int) -> None:
       
        curr_pos = self.position_map[elem]
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        _, weight = self.heap[curr_pos]
        _, parent_weight = self.heap[parent_position]
        if parent_weight > weight:
            self._swap_nodes(parent_position, curr_pos)
            return self._bubble_up(elem)
        return

    def _bubble_down(self, elem: int) -> None:
        
        curr_pos = self.position_map[elem]
        _, weight = self.heap[curr_pos]
        child_left_position = get_child_left_position(curr_pos)
        child_right_position = get_child_right_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight < child_left_weight:
                if child_right_weight < weight:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(elem)
        if child_left_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            if child_left_weight < weight:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(elem)
        else:
            return
        if child_right_position < self.elements:
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight < weight:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(elem)
        else:
            return

    def _swap_nodes(self, node1_pos: int, node2_pos: int) -> None:
        
        node1_elem = self.heap[node1_pos][0]
        node2_elem = self.heap[node2_pos][0]
        self.heap[node1_pos], self.heap[node2_pos] = (
            self.heap[node2_pos],
            self.heap[node1_pos],
        )
        self.position_map[node1_elem] = node2_pos
        self.position_map[node2_elem] = node1_pos


class MaxPriorityQueue:
    def __init__(self) -> None:
        self.heap = []
        self.position_map = {}
        self.elements = 0

    def __len__(self) -> int:
        return self.elements

    def __repr__(self) -> str:
        return str(self.heap)

    def __contains__(self, key: int) -> bool:
        return key in self.position_map

    def is_empty(self) -> bool:
        
        return self.elements == 0

    def push(self, elem: int, weight: int) -> None:
        
        self.heap.append((elem, weight))
        self.position_map[elem] = self.elements
        self.elements += 1
        self._bubble_up(elem)

    def peek_max(self):
        if self.elements == 0:
            raise RuntimeError("Queue is empty")
        elem, _ = self.heap[0]
        return elem

    def extract_max(self) -> int:
      
        if self.elements > 1:
            self._swap_nodes(0, self.elements - 1)
        elem, _ = self.heap.pop()
        del self.position_map[elem]
        self.elements -= 1
        if self.elements > 0:
            bubble_down_elem, _ = self.heap[0]
            self._bubble_down(bubble_down_elem)
        return elem

    def get_priority(self, key: int) -> int:
        if key not in self:
            raise ValueError(f"{key} not found")
        _, weight = self.heap[self.position_map[key]]
        return weight

    def update_key(self, elem: int, weight: int) -> None:
      
        position = self.position_map[elem]
        self.heap[position] = (elem, weight)
        if position > 0:
            parent_position = get_parent_position(position)
            _, parent_weight = self.heap[parent_position]
            if parent_weight < weight:
                self._bubble_up(elem)
            else:
                self._bubble_down(elem)
        else:
            self._bubble_down(elem)

    def _bubble_up(self, elem: int) -> None:
      
        curr_pos = self.position_map[elem]
        if curr_pos == 0:
            return
        parent_position = get_parent_position(curr_pos)
        _, weight = self.heap[curr_pos]
        _, parent_weight = self.heap[parent_position]
        if parent_weight < weight:
            self._swap_nodes(parent_position, curr_pos)
            return self._bubble_up(elem)
        return

    def _bubble_down(self, elem: int) -> None:
       
        curr_pos = self.position_map[elem]
        _, weight = self.heap[curr_pos]
        child_left_position = get_child_left_position(curr_pos)
        child_right_position = get_child_right_position(curr_pos)
        if child_left_position < self.elements and child_right_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight > child_left_weight:
                if child_right_weight > weight:
                    self._swap_nodes(child_right_position, curr_pos)
                    return self._bubble_down(elem)
        if child_left_position < self.elements:
            _, child_left_weight = self.heap[child_left_position]
            if child_left_weight > weight:
                self._swap_nodes(child_left_position, curr_pos)
                return self._bubble_down(elem)
        else:
            return
        if child_right_position < self.elements:
            _, child_right_weight = self.heap[child_right_position]
            if child_right_weight > weight:
                self._swap_nodes(child_right_position, curr_pos)
                return self._bubble_down(elem)
        else:
            return

    def _swap_nodes(self, node1_pos: int, node2_pos: int) -> None:
      
        node1_elem = self.heap[node1_pos][0]
        node2_elem = self.heap[node2_pos][0]
        self.heap[node1_pos], self.heap[node2_pos] = (
            self.heap[node2_pos],
            self.heap[node1_pos],
        )
        self.position_map[node1_elem] = node2_pos
        self.position_map[node2_elem] = node1_pos
