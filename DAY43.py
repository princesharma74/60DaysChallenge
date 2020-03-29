class Node: 
    def __init__(self, data, depth):
        self.data = data
        self.left = None
        self.right = None
        self.depth = depth
#
# Complete the swapNodes function below.
#

def inOrder(root):
    #Write your code here
    if root == None: 
        return
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)

def swap(root, h):
    if root == None:
        return
    if root.depth>=h and root.depth%h == 0:
        temp = root.left
        root.left = root.right
        root.right = temp
    swap(root.left, h)
    swap(root.right, h)
   
from collections import deque
def swapNodes(indexes, queries):
    root = Node(1, 1)
    curr = root
    nodes = deque()
    nodes.append(curr)
    n = 0
    while(n < len(indexes)):
        curr = nodes[0]
        nodes.popleft()
        leftnode = indexes[n][0]
        rightnode = indexes[n][1]
        curr.left = None if leftnode == -1 else Node(leftnode, curr.depth+1)
        curr.right = None if rightnode == -1 else Node(rightnode, curr.depth+1)
        if curr.left !=None and curr.left.data != -1: 
            nodes.append(curr.left)
        if curr.right != None and curr.right.data != -1: 
            nodes.append(curr.right)
        n=n+1
        
    for height in queries:
        swap(root, height)
        inOrder(root)
        print()
    
if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    swapNodes(indexes, queries)
