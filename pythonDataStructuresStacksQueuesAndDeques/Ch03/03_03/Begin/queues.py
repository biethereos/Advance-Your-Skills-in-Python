class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''Takes in an item and inserts that item into the 0th index of the list
        that is representing the Queue.
        
        The runtime is O(n), or linear time, because inserting into the 0th 
        index of the list forces all the other item in the list to move one index
        to the right.
        '''
        
        self.items.insert(0, item)

    def dequeue(self):
        pass
        
    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass
    
my_q = Queue()
my_q.enqueue('apple')
print(my_q.items)
my_q.enqueue('banana')
print(my_q.items)