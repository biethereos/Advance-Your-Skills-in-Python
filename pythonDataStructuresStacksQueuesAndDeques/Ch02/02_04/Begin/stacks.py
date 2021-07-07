class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        """Accepts an item as a parameter and appends it to the end of the list.
        Returns nothing.

        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens in constant time.
        """

        self.items.append(item)

    def pop(self):
        '''Removes and returns last item for the list, which is also 
        the top item of the Stack
        
            Runtime here is constant time, because all it does is index
            to last item of the list'''
        if self.items:
            return self.items.pop()
        
        return None

    def peek(self):
        pass

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