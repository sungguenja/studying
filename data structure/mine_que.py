class Que:
    def __init__(self):
        self.top = []
    
    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)
    
    def clear(self):
        self.top = []

    def push(self,item):
        self.top.append(item)
    
    def pop(self):
        if self.isEmpty():
            return "isEmpty"
        return self.top.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "isEmpty"
        return self.top[-1]
