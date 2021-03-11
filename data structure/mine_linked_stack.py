import mine_node
class LinkedStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def clear(self):
        self.top = None
    
    def push(self,item):
        now_node = mine_node.Node(item,self.top)
        self.top = now_node
    
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    
    def size(self):
        node = self.top
        count = 0
        while node != None:
            count += 1
            node = node.link
        return count