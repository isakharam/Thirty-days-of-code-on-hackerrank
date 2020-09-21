import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        if root==None:
            return Node(data)
        q=[]
        r=[]
        q.append(root)
        
        while(q):
            count=len(q)
            while(count>0):
                temp=q.pop(0)
                r.append(temp.data)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                count-=1
        for i in r:
            print(i,end=' ')
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
