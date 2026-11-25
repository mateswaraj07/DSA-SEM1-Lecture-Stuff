#Implemenatation of BST by ASP Ma'am
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.cnt = 0
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
    def preorder(self,rt):
            if rt is None:
                return
            else:
                print(rt.data,end=" ")
                self.preorder(rt.left)
                self.preorder(rt.right)
    def postorder(self,rt):
            if rt is None:
                return
            else:
                self.postorder(rt.left)
                self.postorder(rt.right)
                print(rt.data,end=" ")
#the logic and execution flow of the preorder and postorder functions are similar to the inorder function, 
# with the main difference being the order in which the nodes are processed. 
# In preorder, the current node is processed before its children, 
# while in postorder, the current node is processed after its children.
    def min_val(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        min_val = current.data
        return min_val

    def max_val(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        max_val = current.data
        return max_val
    
    # def del_node(self,root,val):
    #     # if a node is deleted it is replaced by its inorder successor(left and right child)
    #     # if a node is a left child of its parent, it is replaced by its right child
    #     # if a node is a right child of its parent, it is replaced by its left
    #     # leaf node is deleted directly no replacement is needed
    #     if root is None:
    #         return root
    #     if val<root.data:   #for left subtree
    #         root.left=self.del_node(root.left,val)
    #     elif val>root.data:   #for right subtree
    #         root.right=self.del_node(root.right,val)
    #     else:
    #         if root.left is None: #if the node to be deleted has no left child, return its right child
    #             return root.right
    #         if root.right is None: #if the node to be deleted has no right child, return its left child
    #             return root.left
    #     #When node has both left and right child, find the inorder successor of the node to be deleted
    #     successor=self.get_successor(root)
    #     root.data=successor.data            
    #     root.right=self.del_node(root.right,successor.data)
    #     return root
    def del_node(self,root,val):
        if root is None:
            return root
        if val < root.data:
            root.left = self.del_node(root.left,val)
        elif val > root.data:
            root.right = self.del_node(root.right,val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.get_successor(root)
            root.data = successor.data
            root.right = self.del_node(root.right,successor.data)
        return root

    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp
    
    # Count leaf nodes
    def count_leaf(self, rt):
        if rt is None:
            return
        self.count_leaf(rt.left)
        if rt.left is None and rt.right is None:
            self.cnt += 1
        self.count_leaf(rt.right)

    # Search a node
    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

b=BST()
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(4))
b.insert(Node(65))
b.insert(Node(300))
b.insert(Node(500))
b.insert(Node(50))
print("Inorder Traversal:")
b.inorder(b.root)
print("\nPreorder Traversal:")
b.preorder(b.root)
print("\nPostorder Traversal:")
b.postorder(b.root)
print("\nMinimum Value in BST:", b.min_val())
print("Maximum Value in BST:", b.max_val())
b.del_node(b.root,4) #case1
print("After deleting: ")
b.inorder(b.root)
# Count leaf nodes
b.cnt = 0
b.count_leaf(b1.root)

print("\nTotal no of leaf nodes:", b1.cnt)

# Search node
if b1.search(50):
    print("\nFound the node")
else:
    print("\nNot found")