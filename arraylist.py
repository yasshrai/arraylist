from typing import Any, Optional

class ArrayNode:
    def __init__(self, data: Any = None, nextNode: Optional['ArrayNode'] = None):
        self.data = data
        self.nextNode = nextNode

class ArrayList:
    def __init__(self, head: Optional[ArrayNode] = None, tail: Optional[ArrayNode] = None):
        self.head = head
        self.tail = tail
        self.map: dict[int, ArrayNode] = {}
        self.counter = 0

    def append(self, data: Any):
        newNode = ArrayNode(data)
        if not self.head:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
        self.map[self.counter] = newNode
        self.counter += 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.nextNode
        print("None")

    def __len__(self):
        return self.counter

    def __str__(self):
        string = "["
        current = self.head
        while current:
            if not current.nextNode:
                string += str(current.data)
            else:
                string += str(current.data) + ", "
            current = current.nextNode
        string += "]"
        return string

    def __add__(self, otherList: 'ArrayList') -> 'ArrayList':
        current: ArrayNode = otherList.head
        while current:
            self.append(current.data)
            current = current.nextNode
        return self

    def index(self, value: Any) -> int:
        idx = 0
        current = self.head
        while current:
            if value == current.data:
                return idx
            idx += 1
            current = current.nextNode
        return -1

    def __getitem__(self, key: int) -> Any:
        if key not in self.map:
            raise KeyError("Index out of range")
        return self.map[key].data

    def __setitem__(self, index: int, value: Any):
        if index not in self.map:
            raise KeyError("Index out of range")
        self.map[index].data = value
