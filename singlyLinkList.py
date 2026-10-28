class Node:
    def __init__(self):
         self.data=int(input("Enter data:"))
         self.next=None
class singly:
    def __init__(self):
           self.head=None
    # def InsertAtFirst(self):
    #     if self.head==None:
    #           self.head=Node()
    #     else:
    #          tmp=Node()
    #          tmp.next=self.head
    #          self.head=tmp
    def InsertAtLast(self):
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
                 count=0
                 t=self.head
                 while t!=None:
                      count+=1
                      t=t.next
                 return count

    
#     def mid(self):
#           if self.head==None:
#                print("No nodes are availale") 
#           else:
#                fast=self.head
#                slow=self.head
               
#                while fast!=None and fast.next!=None:
#                     fast=fast.next.next
#                     slow=slow.next   
#                return slow.data  

#     def sum(self):
#          t=self.head
#          total=0
#          while t!=None:
#               total=total+t.data
#               t=t.next
#          return total


#     def deleteFirstNode(self):
#         if self.head==None:
#             print("No Nodes available")
#         else:
#             t=self.head
#             self.head=self.head.next 
#             t.next=None

    def deleteAtSpecificLocation(self):
     position = int(input("Enter position to delete: "))
     totalNodes = self.count()

     if position < 1 or position > totalNodes:
          print("Invalid position")
          return

     if position == 1:
          self.deleteFirstNode()
     elif position == totalNodes:
          self.deleteLastNode()
     else:
          t = self.head
          i = 1

          while i < position - 1:
               t = t.next
               i += 1

          temp = t.next
          t.next = temp.next
          temp.next = None



    def deleteAtLast(self):
        if self.head==None:
            print("No Nodes available")
        elif self.head.next==None:
             self.head=None
        else:
            t=self.head
            while t.next.next!=None:
                 t=t.next
            t.next=None
 
         
    def displayNode(self):
         if self.head==None:
              print("No nodes are available")
         else:
              t=self.head
              while t!=None:
                   print(t.data)
                   t=t.next
              
sl=singly()
# sl.InsertAtFirst()
# sl.InsertAtFirst()
sl.InsertAtLast()
sl.InsertAtLast()
sl.InsertAtLast()
# sl.InsertAtFirst()
print("Total number of nodes are:",sl.count())
# print("middle element is:",sl.mid())
# print("Sum is", sl.sum())
sl.displayNode()
# sl.deleteFirstNode()
# sl.deleteAtSpecificLocation()
sl.deleteAtLast()
sl.displayNode()
    
     