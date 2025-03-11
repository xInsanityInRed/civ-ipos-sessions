"""
Group Activity 1: Stack

UML diagram
Class: Stack
Properties:
    stack: list
    
Methods:
    push(): append
    pop(): pop
    isEmpty(): boolean
"""
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        pass

    def pop(self):
        # check if its empty
        if not self.is_empty():
            return self.stack.pop()
        # if it is empty, return nothing
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Popped item", 

"""
Group Activity 2: Queue

UML DIAGRAM
Class: Queue
Properties:
    queue: list
Methods:
    isEmpty(): boolean
    enqueue(): append
    dequeue(): pop
    peek(): object
"""
class Queue():
    def __init__(self):
        self.list = []

    def enqueue(self, item):
        list.append(item)

    def dequeue(self):
        if list.is_empty():
            return None
        else:
            return list.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            return list[0]

    def is_empty(self):
        return len(list) == 0

my_queue = Queue()
my_queue.push(1)
my_queue.push(2)
my_queue.push(3)
