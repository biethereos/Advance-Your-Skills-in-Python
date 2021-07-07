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
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass