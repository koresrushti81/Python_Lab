class Node():
    def __init__(self):
        self.data=int(input("Enter your data:"))
        self.next=None
class singlyLinkList():
    def __init__(self):
        self.head=None
    def insertdataAtFirst(self):
        if self.head==None:
            self.head=Node()
        else:
            tmp=Node()
            tmp.next=self.head
            self.head=tmp
    def insertdataAtLast(self):
        if self.head==None:
            self.head=Node()
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next=Node()
    def count(self):
        if self.head==None:
            return 0
        else:
            count=1
            t=self.head
            while t.next!=None:
                
                count+=1
                t=t.next
            return count
        
    def sum (self):
        if self.head==None:
            return 0
        else:
            t=self.head
            total=0
            while t!=None:
                total=total+t.data
                t=t.next
            return total
    def mid(self):
        if self .head==None:
            print("No nodes are available")
        else:
             
            fast=self.head
            slow=self.head
            while fast!=None and slow!=None:
                fast=fast.next.next
                slow=slow.next
            return slow
    def insertAtSpecificLocation(self):
              position=int(input("Enter a position:"))
              tNodes=self.count()

              if position>0 and position<=tNodes+1:
                   print("add one node...")
              if position==1:
                  self.insertdataAtFirst()
              elif position==position+1:
                  self.insertdataAtLast()
              else:
                  t=self.head
                  i=1
                  while i<=(position-2):
                       
                      t=t.next
                      i+=1 
                  tmp=Node()
                  tmp.next=t.next
                  t.next=tmp
    def deleteAtfirst(self):
        if self.head==None:
            print("No nodes are available")
        else:
            t=self.head
            self.head=self.head.next
            t.next=None

    def deleteAtLast(self):
        if self.head==None:
            print("No nodes are available")
        elif self.head.next==None:
            self.head=self.head.next
            self.head=None
        
        else:
            t=self.head
            while t.next.next!=None:
                t=t.next
            t.next=None
    def DeleteNodeAtSpecific(self):
        po=int(input("Enter position to delete:"))
        totalNode=self.count()
        if po>0 and po<=totalNode:
            if po==1:
                self.deleteAtfirst()
            elif po==totalNode():
                self.deleteAtLast()
            else:
                t=self .head
                i=1
                while i<=po-2:
                    t=t.next
                    i+=1
                   
                t1=t.next
                t.next=t1.next
                t1.next=None
        else:
            print("Invalid input")        


    def display(self):
        if self.head==None:
            print("No nodes are available")
        else:
            t=self.head
            while t!=None:
                print(t.data)
                t=t.next

sl=singlyLinkList()
sl.insertdataAtLast()
sl.insertdataAtLast()
sl.insertdataAtFirst()
# sl.insertdataAtLast()
# print("Total nodes are :",sl.count())
# print("Sum is", sl.sum())
# print("Middle value is ",sl.mid())

sl.display()
# sl.insertAtSpecificLocation()
print("..........")
# sl.deleteAtfirst()
sl.deleteAtLast()
print(".......")
# sl.deleteAtSpecificLocation()
sl.display()
print(".......")
sl.DeleteNodeAtSpecific()
sl.display()