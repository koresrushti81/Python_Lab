class Node:
    def __init__(self):
        self.data = int(input("Enter data: "))
        self.next = None

class CircularLinkList:
    def __init__(self):
        self.head = None

    def insertNodeAtLast(self):
        if self.head==None:
            self.head = Node()
            self.head.next = self.head
        else:
            t = self.head
            while t.next != self.head:
                t = t.next

            newNode = Node()
            t.next = newNode
            newNode.next = self.head

    def insertAtFirst(self):
        if self.head ==None:
            self.head = Node()
            self.head.next = self.head
        else:
            t = self.head
            while t.next != self.head:
                t = t.next

            newNode = Node()
            newNode.next = self.head
            self.head = newNode
            t.next = self.head

    def countNodes(self):
        if self.head == None:
            return 0
        count = 1
        t = self.head.next
        while t != self.head:
            count += 1
            t = t.next
        return count
    def deleteFirstNode(self):
        if self.head==None:
            print("No nodes are available")
        elif self.head.next==self.head:
            self.head=None
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            self.head=self.head.next
            t.next.next=None
            t.next=self.head
    

    def display(self):
        if self.head == None:
            print("No nodes are available")
        else:
            t = self.head
            while True:
                print(t.data, end=" --> ")
                t = t.next
                if t == self.head:
                    break


cl = CircularLinkList()
cl.insertNodeAtLast()
cl.insertNodeAtLast()
cl.insertNodeAtLast()
cl.insertNodeAtLast()
cl.insertAtFirst()
cl.deleteFirstNode()

print("Total Nodes are", cl.countNodes())
cl.display()
