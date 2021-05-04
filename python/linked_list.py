"""Implement single linked list in python"""
class LinkedList():
    """Linked list class to handle and maintain the LL"""
    __slots__ = '_head', '_min', '_max', '_length'

    def __init__(self):
        self._head = None
    
    def add(self, value):
        current_item = Node()
        current_item._value = value
        current_item._next = None
        if self._head == None:
           self._max = self._min = None 
        if self._max == None or self._max < value:
             self._max = value
        if self._min == None or self._min > value:
             self._min = value
        if self._head == None:
            self._head = current_item
        else: 
            current_item._next, self._head = self._head, current_item 

    def min(self):
        return self._min

    def max(self):
        return self._max

    def exists(self, value):
        if self._max == None or self._min == None or value > self._max or value < self._min or self._head == None:
            return False
        node = self._head
        while node != None:
            if node._value == value:
                return True
            node = node._next
        return False

class Node():
    """DS to implement LL"""
    def __init__(self):
        __slots__ = '_value', '_next'

linked_list = LinkedList()
linked_list.add(5)
linked_list.add(6)
linked_list.add(7)
print(linked_list.exists(5))
print(linked_list.exists(1))
print(linked_list.exists(9))