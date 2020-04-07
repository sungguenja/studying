class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self,node):
        print(node.data, end=' ')
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)



    def postorderTrabersal(self, node):
        if not node.left == None:
            self.postorderTrabersal(node.left)
        if not node.right == None:
            self.postorderTrabersal(node.right)
        print(node.data, end=' ')
    
    def MakeRoot(self,node,left_node,right_node):
        if self.root==None:
            self.root=node
        node.left=left_node
        node.right=right_node
        
node = []
node.append(Node('-'))
node.append(Node('*'))
node.append(Node('/'))
node.append(Node('A'))
node.append(Node('B'))
node.append(Node('C'))
node.append(Node('D'))

m_tree = Tree()
for i in range(int(len(node)/2)):
    m_tree.MakeRoot(node[i],node[i*2+1],node[i*2+2])

print(       '전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)

print('\n' + '후위 순회 : ', end='') ; m_tree.postorderTrabersal(m_tree.root)