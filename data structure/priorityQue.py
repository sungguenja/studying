class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    
    def findMaxIndex(self):
        if self.isEmpty:
            return None
        else:
            highest = 0
            for i in range(1,self.size):
                if self.items[highest]<self.items[i]:
                    highest = i
            return highest
    
    def enque(self,item):
        self.items.append(item)
    
    def deque(self):
        highest = self.findMaxIndex()
        if highest != None:
            return self.items.pop(highest)