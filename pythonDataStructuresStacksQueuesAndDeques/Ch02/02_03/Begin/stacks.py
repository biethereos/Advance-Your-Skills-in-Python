class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        '''Accepts an item as a parameter and append it to end of the list.
            Return nothing
            
            The run time for this method is O(1), or constant time, because appending
            to end of the list happens to constant time 
        '''
        self.items.append(item)

    def pop(self):
        '''Removes and returns last item for the list, which is also 
        the top item of the Stack
        
            Runtime here is constant time, because all it does is index
            to last item of the list
        '''
        if self.items:
            return self.items.pop()
        else:
            return None
    def peek(self):
        return self.items[-1]

    def size(self):
        pass

    def is_empty(self):
        pass
    
    
my_stack = Stack()
my_stack.push('apple')
my_stack.push('banana')
my_stack.push('carrot')
print(my_stack.items)
my_stack.pop()
print(my_stack.items)