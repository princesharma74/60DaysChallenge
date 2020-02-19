#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
class Node:
    def __init__(self, datavalue = None):
        self.dataval = datavalue
        self.nextval = None
class SLinkedList():
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
# e.nextav = Node(343) and e = Node(343) both will work the same way. because you have taken the input in the __input__ function. 
k = SLinkedList()
N = int(input())
temp = None
for i in range(N):
    e = Node(int(input()))
    if k.headval == None:
        k.headval = e
    else:
        temp.nextval = e
    temp = e
k.listprint()
