class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1
        
class BSTAVL:
    def insertNode(self,r,data):
        if r is None:
            r=Node(data)
            return r
        if data < r.data:
            r.left=self.insertNode(r.left,data)
        else:
            r.right=self.insertNode(r.right,data)
            
        r.height=max(self.getHeight(r.left),self.getHeight(r.right))+1
        balancef=self.BF(r) 
        
        #LL
        if balancef > 1 and data < r.left.data:
            return self.rightrotate(r)
        
        #RR:
        if balancef < -1 and data > r.right.data:
            return self.leftrotate(r)
        
        #LR:
        if balancef > 1 and data > root.left.data:
            r.left=self.leftrotate(r.left)
            return self.rightrotate(r)
        
        # RL:
        if balancef < -1 and data < r.right.data:
            r.right=self.rightrotate(r.right)
            return self.leftrotate(r)
        return r
    
    def leftrotate(self,a):
        b=a.right
        c=b.left
        b.left=a
        a.right=c
        
        a.height=max(self.getHeight(a.left),self.getHeight(a.right))+1    
        b.height=max(self.getHeight(b.left),self.getHeight(b.right))+1
        return b    
    
    def rightrotate(self,a):
        b=a.left
        c=b.right
        b.right=a
        a.left=c
        a.height=max(self.getHeight(a.left),self.getHeight(a.right))+1    
        b.height=max(self.getHeight(b.left),self.getHeight(b.right))+1
        return b  
        
    def getHeight(self,node):
        if not node:
            return 0
        return node.height
    

    def BF(self,node):
        if not node:
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)
    
            
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
b=BSTAVL()
root=b.insertNode(root,5)
root=b.insertNode(root,9)
root=b.insertNode(root,7)
b.LOT(root)