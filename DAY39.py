class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None
#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
        
    def insert(self, val):
        node = Node(val)   
        if self.root==None:
            self.root = node
            return
        temp = self.root
        while True: 
            if temp.info < val: 
                if temp.right != None: 
                    temp = temp.right
                    continue
                else: 
                    node = Node(val)
                    temp.right = node
                    break
            if temp.info > val: 
                if temp.left != None: 
                    temp = temp.left 
                    continue
                else: 
                    node = Node(val)
                    temp.left = node
                    break
        return

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
