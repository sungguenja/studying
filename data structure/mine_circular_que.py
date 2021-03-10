class circle_que:
    def __init__(self,max_size):
        self.front = 0
        self.rear = 0
        self.items = [None]*max_size
        self.max_size = max_size
    
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.max_size
    
    def clear(self):
        self.front = 0
        self.rear = 0
    
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.max_size
            self.items[self.rear] = item
        else:
            return "isFull"
    
    def dequeue(self):
        if self.isEmpty():
            return "isEmpty"
        self.front = (self.front + 1) % self.max_size
        return self.items[self.front]
    
    def size(self):
        return (self.rear - self.front + self.max_size) % self.max_size

class circle_deque(circle_que):
    def __init__(self,max_size):
        super().__init__(max_size)
    
    def addRear(self,item):
        self.enqueue(item)
    
    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.items[self.front]
    
    def addFront(self,item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = (self.front-1)%self.max_size
    
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = (self.rear - 1) % self.max_size
            return item
    
    def getRear(self):
        return self.items[self.rear]

