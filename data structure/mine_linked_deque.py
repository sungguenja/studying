import mine_node
class DoubleLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front == None
    
    def clear(self):
        self.front = None
        self.rear = None
    
    def addFront(self,data):
        node = mine_node.DoubleNode(data,None,self.front)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.front.prev = node
            self.front = node
    
    def addRear(self,data):
        node = mine_node.DoubleNode(data,self.rear,None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def deleteFront(self):
        node = self.front
        if node != None:
            data = node.data
            self.front = node.next
            node.next.prev = None
            node.next = None
            return data
    
    def deleteRear(self):
        node = self.rear
        if node != None:
            data = node.data
            self.rear = node.prev
            node.prev.next = None
            node.prev = None
            return data