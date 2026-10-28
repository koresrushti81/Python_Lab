def deleteFirstNode(self):
        if self.head==None:
            print("No Nodes available")
        else:
            t=self.head
            self.head=self.head.next 
            t.next=None
    

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
        totalNodes=self.count()
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