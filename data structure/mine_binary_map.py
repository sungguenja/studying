import mine_node
import mine_binary_search_tree
class BSTMap:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def clear(self):
        self.root = None
    
    def size(self):
        if self.root == None:
            return 0
        else:
            return 1 + self.size(self.root.left) + self.size(self.root.right)
    
    def search(self,key):
        return mine_binary_search_tree.search_bst_recursion(self.root,key)
    
    def search_value(self,value):
        return mine_binary_search_tree.preorder_search(self.root,value)
    
    def insert_node(self,key,value=None):
        node = mine_node.BSTNode(key,value)
        if self.isEmpty():
            self.root = node
        else:
            mine_binary_search_tree.insert(self.root,node)
    
    def delete(self,key):
        self.root = mine_binary_search_tree.delete_bst(self.root,key)
