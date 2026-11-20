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
# The logic of the insert is as follows:
# 1. If the tree is empty, the new node becomes the root.
# 2. If the tree is not empty, we start from the root and compare the new node's data with the current node's data.
# 3. If the new node's data is less than the current node's data,
#    we move to the left child of the current node. If the left child is None, we insert the new node there.
# 4. If the new node's data is greater than or equal to the current node's data,
#    we move to the right child of the current node. If the right child is None, we insert the new node there.

    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
#The logic of the inorder traversal is as follows:
# 1. If the current node is None, we return (base case).
# 2. We recursively call the inorder function on the left child of the current node.
# 3. We print the data of the current node.
# 4. We recursively call the inorder function on the right child of the current node.
#Execution flow above function: 
# The execution flow of the inorder function is as follows:
# 1. The function is called with the root node of the BST.
# 2. The function checks if the current node is None. If it is, the function returns.
# 3. If the current node is not None, the function recursively calls itself on the
#   left child of the current node.
# 4. After the left subtree has been traversed, the function prints the data of the current node.
# 5. The function then recursively calls itself on the right child of the current node.
 
b=BST()
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(0))
b.insert(Node(65))
b.insert(Node(300))
b.inorder(b.root)