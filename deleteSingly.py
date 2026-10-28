# class Node:
#     def __init__(self):
#          self.data=int(input("Enter a number:"))
#          self.next=None
# class singly():
#      def __init__(self):
          
#           self.head=None
#      def insert(self):
#           if self.head==None:
#                self.head=Node()
#           else:
#                t=self.head
#                while t.next!=None:
#                     t=t.next
#                t.next=Node()

#      def display(self):
#           if self.head==None:
#                print("No nodes are available")
#           else:
#                t=self.head
#                while t!=None:
#                     print(t.data)
#                     t=t.next

#      def deleteAtFirst(self):
#           if self.head==None:
#                print("No nodes are available")
#           else:
#                t=self.head
#                self.head=self.head.next 
#                t.next=None
#      def deleteAtlast(self):
#            if self.head==None:
#                print("No nodes are available")
#            elif self.head.next==None:
#                 self.head=None
#            else:
#                 t=self.head
#                 while t.next.next!=None:
                     
#                      t=t.next
#                 t.next=None
#      def count(self):
#           if self.head==None:
#                return 0
#           else:
#                count=0
#                t=self.head
#                while t!=None:
#                     count+=1
#                     t=t.next
#                return count
                    

#     #  def delete (self):
#     #       posi=int(input("Enter position to delete :"))
#     #       c=self.count()
#     #       if posi>0 and posi<=c:
#     #            if posi==1:
#     #                 self.deleteAtFirst()
#     #            elif posi==c:
#     #                 self.deleteAtlast()
#     #            else:
#     #                  i=1
#     #                  t=self.head
#     #                  while i<=posi-2:
#     #                       t=t.next
#     #                       i+=1
#     #                  t1=t.next
#     #                  t.next=t1.next
#     #                  t1.next=None    
#      def delete(self):
#           position1=int(input("Enetr position:"))
#           co=self.count()
#           if position1 >0 and position1<=co:
#                if position1==1:
#                     self.
#                elif position1==co:
#                     self.i
                    
               
          
                
      

# sl=singly()
# sl.insert()
# sl.insert()
# sl.insert()
# sl.insert()
# print("count is",sl.count())
# # sl.display()
# # sl.deleteAtFirst()
# sl.deleteAtlast()
# sl.display()
# sl.delete()
# sl.display()
               