'''
creating a stack:
push: 
pop: 
isEmpty: 
isFull: 
Peek 
'''
class stacks: 
    #constructor to initialize the stack 
    def __init__(self, size): 
        self.arr = [None] * size 
        self.capacity = size 
        self.top = -1

    def create_stack():
        stack = []
        return stack 

    def isEmpty(stack):
        return len(stack) == 0

    def isFull(stack):
        return len()

    def push(stack, item):
        stack.append(item)
        print("pushed item: " +item)

    def pop(stack): 
        stack.pop(item)
        print("popped item: " +item)