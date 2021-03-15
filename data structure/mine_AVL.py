import mine_binary_map
def LLRotate(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def RRRotate(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def RLRotate(A):
    B = A.right
    A.right = LLRotate(B)
    return RRRotate(A)

def LRRotate(A):
    B = A.left
    A.left = RRRotate(B)
    return LLRotate(A)

def calc_height(n):
    if n == None:
        return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    if hleft>hright:
        return hleft + 1
    else:
        return hright + 1

def rebalance(parent):
    hleft  = calc_height(parent.left)
    hright = calc_height(parent.right)
    hdiff  = hleft - hright

    if hdiff > 1:
        if calc_height(parent.left.left) - calc_height(parent.left.right) > 0:
            parent = LLRotate(parent)
        else:
            parent = LRRotate(parent)
    elif hdiff < -1:
        if calc_height(parent.right.left) - calc_height(parent.right.left) < 0:
            parent = RRRotate(parent)
        else:
            parent = RLRotate(parent)
    
    return parent

def insert_avl(parent,node):
    if parent.key < node.key:
        if parent.right == None:
            parent.right = node
        else:
            parent.right = insert_avl(parent.right,node)
        return rebalance(parent)
    
    elif parent.key > node.key:
        if parent.left == None:
            parent.left = node
        else:
            parent.left = insert_avl(parent.left,node)
        return rebalance(parent)
    
    else:
        print("key값 중복")

class AVLMap(mine_binary_map.BSTMap):
    def __init__(self):
        super().__init__(self)
    
    def insert(self,key,value=None):
        node = mine_binary_map.BSTMap(key,value)
        if self.isEmpty():
            self.root = node
        else:
            self.root = insert_avl(self.root,node)