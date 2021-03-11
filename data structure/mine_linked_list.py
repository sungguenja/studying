import mine_node
class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.top == None
    
    def clear(self):
        self.top = None
    
    def push(self,item):
        now_node = mine_node.Node(item,self.top)
        self.top = now_node

    def size(self):
        node = self.top
        count = 0
        while node != None:
            count += 1
            node = node.link
        return count
    
    def getNode(self,position):
        if position<0:
            return None
        
        node = self.head
        while position>0 and node != None:
            node = node.link
            position -= 1
        return node
    
    def getValue(self,position):
        node = self.getNode(position)
        if node == None:
            return None
        else:
            return node.data
    
    def replace(self,item,position):
        node = self.getNode(position)
        if node != None:
            node.data = item
        
    def find(self,data):
        node = self.head
        while node != None:
            if node.data == data:
                break
            node = node.link
        return node
    
    def insert(self,position,data):
        node = self.getNode(position-1)
        if node == None:
            self.head = mine_node.Node(data,self.head)
        else:
            insert_node = mine_node.Node(data,node.link)
            node.link = insert_node
    
    def delete(self,position):
        node = self.getNode(position-1)
        if node != None:
            if self.head != None:
                self.head = self.head.link
        elif node.link != None:
            node.link = node.link.link