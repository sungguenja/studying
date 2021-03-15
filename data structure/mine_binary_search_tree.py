import mine_node
def search_bst_recursion(n,key):
    if n == None:
        return None
    elif n.key == key:
        return n
    elif n.key > key:
        return search_bst_recursion(n.left,key)
    elif n.key < key:
        return search_bst_recursion(n.right,key)

def search_bst_while(n,key):
    while n!=None:
        if n.key == key:
            return n
        elif n.key < key:
            n = n.right
        elif n.key > key:
            n = n.left
    return None

def preorder_search(n,value):
    if n == None:
        return None
    if n.value == value:
        return n
    res = preorder_search(n.left,value)
    if res != None:
        return res
    else:
        return preorder_search(n.right,value)

def inorder_search(n,value):
    if n==None:
        return None
    res = inorder_search(n.left,value)
    if res != None:
        return res
    else:
        if n.value == value:
            return n
        else:
            return inorder_search(n.right,value)

def insert(n,r):
    if n.key < r.key:
        if r.left == None:
            r.left = n
            return True
        else:
            return insert(n,r.left)
    elif n.key > r.key:
        if r.right == None:
            r.right = n
            return True
        else:
            return insert(n,r.right)
    else:
        return False

def delete_only_node(parent,node,root):
    if parent == None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
    return root

def delete_has_one_child(parent,node,root):
    child = None
    if node.left != None:
        child = node.left
    elif node.right != None:
        child = node.right
    
    if child == None: # 잘못된 루트 삭제를 할려는 경우
        return None
    
    if node == root:
        root = child
    else:
        if parent.left == node:
            parent.left = node
        elif parent.right == node:
            parent.right = node
    return root

def delete_has_both_node(parent,node,root):
    successor_parent = node
    successor = node.right
    while node.left != None:
        successor_parent = successor
        successor = successor.left
    
    if successor_parent.left == successor:
        successor_parent.left = successor.right
    elif successor_parent.right == successor:
        successor_parent.right = successor.right
    
    node.key = successor.key
    node.value = successor.value
    node = successor

    return node

def delete_bst(root,key):
    if root == None:
        return None
    
    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if node.key < key:
            node = node.right
        else:
            node = node.left
    
    if node == None:
        return None
    if node.left == None and node.right == None:
        root = delete_only_node(parent,node,root)
    elif node.left == None or node.right == None:
        root = delete_has_one_child(parent,node,root)
    else:
        root = delete_has_both_node(parent,node,root)
    return root