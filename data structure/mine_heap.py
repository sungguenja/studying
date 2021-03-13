class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)  # 0번 항목은 사용하지 않는다

    def size(self):
        return len(self.heap) - 1
    
    def isEmpty(self):
        return self.size() == 0
    
    def Parent(self,i):
        return self.heap[i//2]
    
    def left(self,i):
        return self.heap[2*i]
    
    def right(self,i):
        return self.heap[2*i+1]
    
    def insert(self,number):
        self.heap.append(number)
        i = self.size()
        while i>=1 and number > self.Parent(i):
            self.heap[i] = self.heap[i//2]
            i = i//2
        self.heap[i] = number
    
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while child < self.size():
                if child<self.size() and self.left(parent) < self.right(parent):
                    child += 1
                    # 기본은 왼쪽 자식을 보는데 오른쪽 자식이 클 경우 오른쪽 자식으로 타겟 변경
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child = child * 2
            
            self.heap[parent] = last
            self.heap.pop()
            return hroot