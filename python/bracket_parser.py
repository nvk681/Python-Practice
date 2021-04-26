"""Using stack to parse brackets
    The input will only pare the brackets [], {}, () and ignore anything in between them
    So we can enter any expressions and check it.
"""

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

initial_stack = ArrayStack()
secondary_stack = ArrayStack()
TUPLE_OF_BRACKETS = ("[", "]", "{", "}", "(", ")")
TUPLE_OF_CLOSING_BRACKETS = ("]", "}", ")")
PAIRING_BRACKETS = {'[':']', '{':'}', '(':')'}

for parsed_item in list(item for item in list(input("Please enter your expression in a single line : => ")) if item in TUPLE_OF_BRACKETS):
    initial_stack.push(parsed_item)

while not initial_stack.is_empty():
    if initial_stack.top() not in TUPLE_OF_CLOSING_BRACKETS and  secondary_stack.is_empty():
        print("Unmatched")
        exit()

    if initial_stack.top() in TUPLE_OF_CLOSING_BRACKETS:
        secondary_stack.push(initial_stack.pop())
    else:
        if PAIRING_BRACKETS[initial_stack.top()] == secondary_stack.top():
            initial_stack.pop();secondary_stack.pop()
        else:
            print("Unmatched")
            exit()

print("Matched")
exit()
