class Node:
    def __init__(self):
        self.data = int(input("Enter Data: "))
        self.next = None


class SinglyLinkList:
    def __init__(self):
        self.head = None

    def insertNodeAtLast(self):
        if self.head == None:
            self.head = Node()
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = Node()

    def insertNodeAtFirst(self):
        t = Node()
        t.next = self.head
        self.head = t  
    # def insertAtSpecificLocation(self):
    #     position=int(input("enter position:"))
    #     totalNodes=self.countNode()
    #     if position >0 and position<=totalNodes+1:
    #       if position==1:
    #         self.insertNodeAtFirst()
    #       elif position==totalNodes+1:
    #         self.insertNodeAtLast()
    #       else:
    #         t=self.head
    #         i=1
    #         while i<=(position-2):
    #            t=t.next
    #            i=i+1
    #         temp=Node()
    #         temp.next=t.next
    #         t.next=temp
    #     else:
    #         print("invalid location")
    def deleteFirstNode(self):
        if self.head==None:
            print("No Nodes available")
        else:
            t=self.head
            self.head=self.head.next 
            t.next=None
            print("invalid location")
    def deleteLastNode(self):
        if self.head==None:
            print("No Nodes available")
        elif self.head.next==None:
            self.head=None
        else:
            t=self.head
            while t.next.next!=None:
                t=t.next
            t.next=None
    def deleteAtSpecificLocation(self):
        position1=int(input("enter position for deletion:"))
        totalNodes=self.countNode()
        if position1 >0 and position1<=totalNodes:
          if position1==1:
            self.deleteFirstNode()
          elif position1==totalNodes:
            self.deleteLastNode()
          else:
            t=self.head
            i=1
            while i<=(position1-2):
               t=t.next
               i=i+1
            t1=t.next
            t.next=t1.next
            t1.next=None
             
    #     else:
    #         print("invalid location")
    # def display(self):
    #     if self.head == None:
    #         print("No nodes available")
    #     else:
    #         t = self.head
    #         while t != None:
    #             print(t.data)
    #             t = t.next
    # def deleteNodeByItValue(self):
    #     value=int(input("enter Node value which u want to delete :"))
    #     if(self.head==None):
    #         print("No nodes are available ")
    #     else:
    #         t=self.head

    #         while t.data==value:
    #             self.deleteFirstNode()
    #             t=self.head
    #         while t.next.data==value:
    #             t1=t.next
    #             t.next=t1.next
    #             t1.next=None

    # def sum(self):
    #  if self.head== None:
    #     print("No nodes are available")
    #  else:
    #     total = 0
    #     t = self.head
    #     while t!= None:
    #         total = total + t.data
    #         t = t.next
    #     print("Sum =", total)

                
    # def countNode(self):
    #     count = 0
    #     t = self.head
    #     while t != None:
    #         count += 1
    #         t = t.next
    #     return count
    
    def traverse (self):
        t=self.head
        while t.next!=None:
            print(t.data)
            t=t.data
            
        

    def mid(self):
        fast=self.head
        slow=self.head
        while (fast.data!=None or slow.data!=None):
            fast=fast.next.next
            slow=slow.next
            print(slow)

sl = SinglyLinkList()
sl.insertNodeAtLast()
sl.insertNodeAtLast()
sl.insertNodeAtLast()
# sl.sum()

# sl.insertAtSpecificLocation()
sl.deleteFirstNode()
# sl.deleteLastNode()
# sl.deleteNodeByItValue()
# sl.deleteAtSpecificLocation()
# sl.display()
sl.traverse()
sl.mid()
# print("Total nodes:", sl.countNode())
 
 