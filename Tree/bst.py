#Implemenatation of BST by ASP Ma'am
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,newnode):
        if self.root is None:   #IF BST IS EMPTY
            self.root=newnode
        else:
            temp=self.root
            while True:
                if newnode.data<temp.data:
                    if temp.left is None:
                        temp.left=newnode
                        return
                    else:   
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=newnode
                        return
                    else:
                        temp=temp.right