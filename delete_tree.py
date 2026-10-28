class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BT:
    def insertNode(self,r,data):
        if r is None:
            r=Node(data)
            return r
        if data < r.data:
            r.left=self.insertNode(r.left,data)
        else:
            r.right=self.insertNode(r.right,data)
        return r
    
    def findminvalue(self,r1):
        curr=r1
        while curr.left:
            curr=curr.left
        return curr  
          
    def delete(self,r,key):
        if r is None:
            return r
        if key < r.data:
            r.left=self.delete(r.left,key)
        elif key > r.data:
            r.right=self.delete(r.right,key)
        
        else:
            # no child
            if r.left is None and r.right is None:
                return None
            # one child
            if r.left is None:
                return  r.right
            elif r.right is None:
                return r.left
            # two child
            
            minval=self.findminvalue(r.right)
            r.data=minval.data
            r.right=self.delete(r.right,minval.data)
        return r
            
    def LOT(self,r):
        if r is None:
            return 
        que=[]
        que.append(r)
        while que:
            curr=que.pop(0)
            print(curr.data,end=" ") 
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            
root=None
b=BT()
root=b.insertNode(root,45)
root=b.insertNode(root,34)
root=b.insertNode(root,23)
root=b.insertNode(root,78)
root=b.insertNode(root,90)
root=b.insertNode(root,22)
root=b.insertNode(root,56)
root=b.insertNode(root,40)
root=b.insertNode(root,67)
b.LOT(root)
root=b.delete(root,45)
print("after delete")
b.LOT(root)