class Node:
    def __init__(self):
        self.data=int(input("Enter data:"))
        self.next=None
        self.pre=None
class DoublyLinkList:
    def __init__(self):
         self.head=None

    def insertNodeAtLast(self):
        if(self.head==None):
            self.head=Node()
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            
            t.next=Node()
            t.next.pre=t
    def insertNodeAtFirst(self):
        if self.head==None:
            self.head=Node()
        else:
            tmp=Node()
            tmp.next=self.head
            tmp.next.pre=tmp
            self.head=tmp
    def count(self):
        if self.head==None:
            return 0
        else:
            count=0
            t=self.head
            while t!=None:
                count+=1
                t=t.next
            return count
    def delete(self):
        if self.head==None:
            print("No nodes are available")
        else:
            t=self.head
            while t.next!=None:
                t=t.next
                t.next=None
                t.next.pre=None
            # self.head=self.head.next
            # self.head.pre.next=None
            # self.head.pre=None


            
           
    def display(self):
        if self.head == None:
            print("No nodes available")
        else:
            t = self.head
            while t != None:
                print(t.data)
                t = t.next
 
     

dl=DoublyLinkList()
dl.insertNodeAtLast()
dl.insertNodeAtLast()
dl.insertNodeAtLast()
dl.insertNodeAtLast()
dl.insertNodeAtFirst()
print("Count is:",dl.count())
dl.delete()
dl.display()
 
 