class Node:
 def __init__(self):
   self.data=int(input("Enter data:")) 
   self.next=None
   self.pre=None
class doublyLinkList:
  def __init__(self):
    self.head=None
  def insertAtFirst(self):
    if self.head==None:
      self.head=Node()
    else:
       tmp=Node()
       tmp.next=self.head
       self.head=tmp
  def insertAtLast(self):
    if self.head==None:
      self.head=Node()
    else:
       t=self.head
       while(t.next!=None):
         t=t.next
       t.next=Node()
  def insertAtSpecificLocation(self):
      position=int(input("Enter position:"))
      if position==1:
        dl.insertAtfirst()
      elif position==position+1:
        dl.insertAtLast()
      else:
        t=self.head
        while position-2:
          t=t.next
        t.next=Node()
  def countNodes(self):
    if self.head==None:
      return 0
    else:
      t=self.head
      count=1
      while t!=None:
        count+=1
      return count
  def displayAllNodesInRevereseOrder(self):
        if self.rev==None:
            print("No Nodes Are Available")
        else:
            t=self.rev
            while t!=None:
                print(t.data,end="<==>")
                t=t.pre

  def deleteLastNode(self):
     if self.head==None:
        print("No nodes available")
     elif self.head.next==None:
        self.head==None
        self.rev==None
     else:
        t=self.head
        while t.next.next!=None:
           t=t.next
        t.next.pre= None
        t.next=None
        self.rev=t

  def display(self):
    if self.head==None:
      print("No nodes are available.")
    else:
      t=self.head
      while t!=None:
        print(t.data,end=" ")
        t=t.next

dl=doublyLinkList()
while True:
    print("\nMenu:")
    print("1.Insert Node At Last")
    print("2.Insert Node At First")
    print("3.Insert Node At Specific Location")
    print("4.Display All Nodes")
    print("5.Display All Nodes In Reverse Order")
    print("6.Count Nodes")
    print("7.delete last Node")
    choice=int(input("\nEnter Your Choice:"))
    match choice:
        case 1:
            dl.insertAtLast()
        case 2:
            dl.insertAtFirst()
        case 3:
            dl.insertAtSpecificLocation()
        case 4:
            dl.display()
        case 5:
            dl.displayAllNodesInRevereseOrder()
        case 6:
            print("Total Nodes:",dl.countNodes())
        case 7:
          dl.deleteLastNode()
        case 100:
            exit(0)
    