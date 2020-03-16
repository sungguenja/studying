class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self,node):
        print(node, end=' ')
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self):
        if not node.left == None:
            self.inorderTraversal(node.left)
        print(node, end=' ')
        if not Node.right == None:
            self.inorderTraversal(node.right)

    def postorderTrabersal(self, node):
        if not node.left == None:
            self.postorderTraversal(node.left)
        if not node.right == None:
            self.postorderTrabersal(node.right)
        print(node, end=' ')
    
    def MakeRoot(self,node,left_node,right_node):
        if self.root==None:
            self.root=node
        node.left=left_node
        node.right=right_node
        