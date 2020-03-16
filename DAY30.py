class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        newNode = SinglyLinkedListNode(node_data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            self.tail = current.next
def print_singly_linked_list(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next
int_arr = list(map(int, input().split()))
sl = SinglyLinkedList()
for i in range(len(int_arr)):
    sl.insert_node(int_arr[i])
    temp = sl.head
print_singly_linked_list(temp)
