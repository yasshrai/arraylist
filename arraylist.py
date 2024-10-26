from typing import Any

class ArrayNode:
    def __init__(self,data = None,nextNode = None):
        self.data = data
        self.nextNode = nextNode

class ArrayList:
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail
        self.map = dict()
        self.counter = 0
    def append(self,data:Any):
        newNode = ArrayNode(data)
        if not self.head:
            self.tail = newNode
            self.head = newNode
            self.map[self.counter] = newNode
            self.counter += 1
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
            self.map[self.counter] = newNode
            self.counter += 1
    def display(self):
        current = self.head
        while current:
            print()
    def __len__(self):
        return self.counter
    
    def __str__(self):
        string = "["
        current = self.head
        while current:
            if  not current.nextNode:
                string = string + str(current.data)
            else:
                string = string + str(current.data) + ", "
            current = current.nextNode
        string += "]"
        return string
    def __add__(self,otherList):
        otherList:ArrayList
        current:ArrayNode = otherList.head
        while current:
            self.append(current.data)
            current = current.nextNode
        return self
    
    def index(self,value):
        idx = 0
        current = self.head
        while current:
            if value == current.data:
                return idx
            idx +=1
            current = current.nextNode
        
        return -1
    def __getitem__(self,key):
        if not self.head:
            raise KeyError
        return self.map[key].data
