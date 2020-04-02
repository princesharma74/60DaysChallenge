# Enter your code here. Read input from STDIN. Print output to STDOUT
var = list(map(int, input().split()))
#print(var)
n = var[0]
q = var[1]

nodes = []
sets = []
for i in range(n-1): 
    nodes.append(list(map(int, input().split())))
#print(nodes)

for i in range(q): 
    a = int(input())
    b = list(map(int, input().split()))
    sets.append(b)
'''
print("q: ", q)
print("n: ", n)
print("nodes: ", nodes)
print("sets: ", sets)
'''
#DEFINITION OF NODE
class Node: 
    def __init__(self, data): 
        self.data = data
        self.link = []

    def appender(self, link): 
        self.link.append(link)
lst = []

#BELOW IS MAKING TREE BASED ON THE ENTERED INPUTS
for nodeINPUT in nodes: 
    if len(lst) == 0: 
        node1 = Node(nodeINPUT[0])
        node2 = Node(nodeINPUT[1])
        lst.append(node1)
        lst.append(node2)
    else: 
        for i in range(len(lst)): 
            if lst[i].data == nodeINPUT[0]: 
                node1 =lst[i]
                break
            else: 
                node1 = Node(nodeINPUT[0])
                if i == len(lst)-1: 
                    lst.append(node1)

        for i in range(len(lst)): 
            if lst[i].data == nodeINPUT[1]: 
                node2 =lst[i]
                break
            else: 
                node2 = Node(nodeINPUT[1])
                if i == len(lst)-1: 
                    lst.append(node2)
    node1.appender(node2)
    node2.appender(node1)


'''
def levelofnode(root, key, level, avoid): 
    if root == None: 
        return -1
    if root.data == key: 
        return level
    for i in range(len(root.link)): 
        if i != avoid or avoid == -1: 
            print('IT Ran! at', i)
            avoid = root.link[i].link.index(root)
            l = levelofnode(root.link[i], key, level+1, avoid)
            if l != -1 and l != None: 
                return l
            if i == (len(root.link)-1): 
                return levelofnode(root.link[i], key, level+1, avoid)
avoid = -1 #root address is not in it's link itself
print('OUTPUT OF THE FUNCTION IS:', levelofnode(root, 2, 0, avoid))
'''
#THIS FINDS OUT THE DISTANCE BETWEEN TWO NODES. HERE ROOT IS THE ADDRESS OF THE VALUE V1 AND 'AVOID' MAKES SURE IT DOES NOT COME BACK.
def dist(root, v2, avoid): 
    if root == None: 
        return -1
    if root.data == v2: 
        return 0
    for i in range(len(root.link)): 
        if i != avoid or avoid == -1: 
            avoid = root.link[i].link.index(root)
            if dist(root.link[i], v2, avoid) != None: 
                l = 1 + dist(root.link[i], v2, avoid)
            else: 
                continue
            if l != -1 and l != None: 
                return l

'''
root.link.append(root)
def lca(root, v1, v2): 
    i = 0
    for node in root.link: 
        if i == 0:
            if node != root and root.data > max(v1, v2):
                return lca(root.link[i], v1, v2)
        else:  
            if node != root and root.data < min(v1, v2):

            
'''
from itertools import combinations
for SET in sets: 
    if len(SET) != 1: 
        total = 0
        for pair in combinations(SET, 2): 
            for node in lst: 
                if node.data == pair[0]: 
                    root = node
            total = total + pair[0]*pair[1]*dist(root, pair[1], -1)
        print(total%1000000007)
    else:
        print(0)

