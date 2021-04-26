"""Implement stack using list"""
class Empty(Exception):
    """Empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a list"""

    def __init__(self):
        """Create an empty list"""
        # nonpublic list instance
        self._data = []

    def __len__(self):
        """Return the length"""
        return len(self._data)

    def is_empty(self):
        """check if stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element to the stack"""
        # new item stored at end of list
        self._data.append(e)

    def top(self):
        """Get value without poping the element"""
        if self.is_empty():
            raise Empty("Stack is empty")
            # the last item in the list
        return self._data[-1]

    def pop(self):
        """Pop element from the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        # remove last item from list
        return self._data.pop()
