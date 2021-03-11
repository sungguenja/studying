import mine_node
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    
    def isEmpty(self):
        return self.tail == None
    
    def clear(self):
        self.tail = None
    
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    
    def enqueue(self,data):
        node = mine_node.Node(data)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail == self.tail.link:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data