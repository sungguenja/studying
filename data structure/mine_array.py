class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, position, element):
        self.items.insert(position,element)

    def delete(self,position):
        return self.items.pop(position)

    def isEmpty(self):
        return len(self.items) == 0
    
    def getElement(self,position):
        return self.items[position]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []
    
    def find(self,item):
        return self.items.index(item)
    
    def replace(self,position,item):
        self.items[position] = item
    
    def sort(self):
        self.items.sort()
    
    def merge(self,array):
        self.items.extend(array)

    def display(self,message="ArrayList : "):
        print(message, self.size(), self.items)