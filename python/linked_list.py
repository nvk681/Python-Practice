"""Implement single linked list in python"""
class LinkedList():
    """Linked list class to handle and maintain the LL"""
    __slots__ = '_head', '_min', '_max', '_length'

    def __init__(self):
        self._head = None
        self._length = 0

    def add(self, value):
        """Add item into the linked list """
        current_item = Node()
        current_item._value = value
        current_item._next = None
        if self._head is None:
            self._max = self._min = None
        if self._max is None or self._max < value:
            self._max = value
        if self._min is None or self._min > value:
            self._min = value
        if self._head is None:
            self._head = current_item
        else:
            current_item._next, self._head = self._head, current_item
        self._length += 1

    def min(self):
        """Get the smallest element in the LL """
        return self._min

    def max(self):
        """Get the biggest element in the LL """
        return self._max

    def exists(self, value):
        """Check if the element exists in the LL """
        if self._head is None:
            return False
        if self._max is None or self._min is None or value > self._max or value < self._min:
            return False
        node = self._head
        while node is not None:
            if node._value == value:
                return True
            node = node._next
        return False

    def delete(self, value):
        """ Remove a value from the LL """
        if self._max is None or self._min is None or value > self._max or value < self._min or self._head is None:
            return False
        prev = self._head
        if prev._value == value:
            self._head = None
        elif prev._next is None:
            return False
        node = prev._next

        while node is not None:
            if node._value == value:
                prev._next = node._next
                self._length -= 1
                return True
            prev, node = node, node._next

        return False

    def length(self):
        return self._length

class Node():
    """DS to implement LL"""
    def __init__(self):
        __slots__ = '_value', '_next'

linked_list = LinkedList()
linked_list.add(5)
linked_list.add(6)
linked_list.add(7)
print(linked_list.exists(5))
print(linked_list.delete(5))
print(linked_list.exists(9))
