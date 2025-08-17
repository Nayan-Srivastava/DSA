# Creating a Stack using a Linked List:

class Node: # A node in the linked list
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # A stack implemented using a linked list

    def __init__(self): # Initialize an empty stack
        self.head = None

    def is_empty(self): # Check if the stack is empty
        return self.head is None

    def push(self, data): # Push an item onto the stack
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self): # Pop an item from the stack
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def peek(self): # Peek at the top item of the stack without removing it
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data

stack = Stack()
# Example usage:
# Pushing an item onto the stack
stack.push(10)
stack.push(20)
# Peeking at the top item of the stack
print(stack.peek())  # Output: 20
# Popping an item from the stack
print(stack.pop())   # Output: 20
# Checking if the stack is empty
print(stack.is_empty())  # Output: False
# Popping another item from the stack
print(stack.pop())   # Output: 10
# Checking if the stack is empty again
print(stack.is_empty())  # Output: True
# Attempting to pop from an empty stack will raise an error
try:
    stack.pop()  # This will raise an IndexError
except IndexError as e:
    print(e)