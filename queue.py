class Node:
    def __init__(self):
         self.data=int(input("Enter data:"))
         self.next=None
class queue:
     def __init__(self):
           self.top=None
     def enqueue(self):
          if self.top==None:
               self.top=Node()
          else:
               t=self.top
               while t.next!=None:
                    t=t.next
               t.next=Node()
     def dequeue(self):
          if self.top==None:
               print("No nodes are available.")
          else:
                t=self.top
                self.top=self.top.next
                t.next=None
     def traversal(self):
          if self.top==None:
               print("No nodes are available.")
          else:
               t=self.top
               while t!=None:
                    print(t.data)
                    t=t.next
q=queue()
while True:
     print("Menu:")
     print("1.enqueue") 
     print("2.dequeue") 
     print("3.traversal") 
     print("100.exit")
     choice=int(input("Enter your choice:"))
     match choice:
          case 1:
               q.enqueue()
          case 2:
               q.dequeue()
          case 3:
               q.traversal()
          case 100:
               exit(0)
              
                    