class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        """Takes an item as a parameter and inserts it into the 0th index
        of the list that is representing the Deque.

        The runtime is linear, or O(n), because every time you insert into the
        front of a list, all the other items in the list need to shift one
        position to the right.
        """

        self.items.insert(0, item)

    def add_rear(self, item):
        """Takes in an item as aparameter and appends that item to the end of
        the list that is representing the Deque.

        The runtime is constant because appending to the end of a list happens
        in constant time.
        """

        self.items.append(item)

    def remove_front(self):
        '''Removes and returns the item in the 0th index of the list, which
        represents the front of the Deque.

        The runtime is linear, or O(n), because when we remove an item from the
        0th index, all the other items have to shift one index to the left.
        '''
        if self.items:
            return self.items.pop(0)
        return None
    def remove_rear(self):
        '''Removes and returns the last item of the list, which represents the
        rear of the Deque.

        The runtime is constant because all we're doing is indexing to the end
        of a list.
        '''
        return self.items.pop()

    def peek_front(self):
        pass

    def peek_rear(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

my_d = Deque()
my_d.add_front('apple')
my_d.add_front('banana')
my_d.add_front('carrot')
print(my_d.items)
my_d.remove_front()
print(my_d.items)
my_d.remove_rear()
print(my_d.items)