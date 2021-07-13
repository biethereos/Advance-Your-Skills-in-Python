class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'SLLNode object: data = {self.data}'
    
    def get_data(self):
        '''Return the self.data attribute.'''
        return self.data

    def set_data(self, new_data):
        '''Replace the existing value of the self.data attribute with new_data
        parameter.'''
        self.data = new_data

    def get_next(self):
        '''Return the self.next attribute'''
        return self.next

    def set_next(self, new_next):
        '''Replace the existing value of the self.next attribute with new_next
        parameter.'''
        self.next = new_next

node = SLLNode('apple')
print(node.get_data())
node.set_data(7)
print(node.get_data())
node2 = SLLNode('carrot')
node.set_next(node2)
print(node.get_next())
