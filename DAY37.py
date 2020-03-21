class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)

Tree: Level Order Traversal
"""
from collections import deque
def levelOrder(root):
    #Write your code here
    q = deque()
    q.append(root)
    if root == None: 
        print()
    try: 
        while True:
            current = q[0]
            print(current.info, end=" ")
            if current.left!=None: 
                q.append(current.left)
            if current.right!=None: 
                q.append(current.right)
            q.popleft()
    except IndexError: 
        print(end="")



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
