class LinearProbing:
    def __init__(self,size):
        self.M = size
        self.a = [None]*size    # a 해시테이블 (키값저장)
        self.d = [None]*size    # d 데이터 저장용
    
    def hash(self,key):
        return key % self.M
    
    def put(self,key,data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                break
    
    def get(self,key):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position + j) % self.M
            if i == initial_position:
                return None
        return None

class Chaining:
    class Node:
        def __init__(self,key,data,link=None):
            self.key = key
            self.data = data
            self.link = link
    
    def __init__(self,size):
        self.M = size
        self.A = [None]*size

    def hash(self,key):
        return key % self.M
    
    def put(self,key,data):
        i = self.hash(key)
        p = self.A[i]
        while p != None:
            if key == p.key:
                p.data = data
                return
            p = p.link
        self.A[i] = self.Node(key,data,self.A[i]) # 맨 앞에 삽입