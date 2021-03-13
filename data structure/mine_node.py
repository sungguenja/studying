class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link

class DoubleNode:
    def __init__(self,elem,prev_node=None,next_node=None):
        self.data = elem
        self.prev = prev_node
        self.next = next_node

class TNode:
    def __init__(self,elem,left=None,right=None):
        self.data = elem
        self.left = left
        self.right = right