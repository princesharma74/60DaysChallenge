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
"""
from collections import deque
l1 =[]
def LevelTraversal(root): 
    m = deque()
    if root == None: 
        return l1
    m.append(root)
    try: 
        while True: 
            current = m[0]
            l1.append(current.info)
            if current.left!=None: 
                m.append(current.left)
            if current.right!=None:
                m.append(current.right)
            m.popleft()
    except: 
        pass
    return l1

def VerticalTraversal(root, hd, m): 
    if root == None: 
        return
    try: 
        m[hd].append(root.info)
    except: 
        m[hd] = [root.info]
    VerticalTraversal(root.left, hd-1, m)
    VerticalTraversal(root.right, hd+1, m)

def VerticalTraversalList(root): 
    l2 = []
    hd = 0
    m = dict()
    VerticalTraversal(root, hd, m)
    for i in sorted(m): 
        l2.append(m[i])
    return l2

def topView(root):
    #Write your code here
    l1 = LevelTraversal(root)
    #print(l1)
    l2 = VerticalTraversalList(root)
    #print(l2)
    for i in l2:
        compare = []
        for j in i:
            #print(j, l1.index(j))
            compare.append(l1.index(j))
        min1 = min(compare)
        print(l1[min1], end=' ')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
