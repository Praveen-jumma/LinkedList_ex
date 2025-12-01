class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        nn = Node(data)
        nn.next = self.head
        self.head = nn
    def insert_at_end(self,data):
        nn = Node(data)
        temp = self.head
        while temp.next != None :
          temp = temp.next
        temp.next = nn



    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

L1 = LinkedList()
L1.insert_at_first(12)
L1.insert_at_first(14)
L1.insert_at_first(16)
L1.insert_at_end(20)
L1.insert_at_end(50)
L1.display()
