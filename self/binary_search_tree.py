
# BST Implementation using Linked List

# Creating Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creating BST
class BST:
    def __init__(self):
        self.root = None
# Insertion
    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root

            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right

    # Inorder Traversal
        def inorder(self, temp):
            if temp is not None:
                self.inorder(temp.left)
                print(temp.data, end=" ")
                self.inorder(temp.right)
    
        # Preorder Traversal
        def preorder(self, temp):
            if temp is not None:
                print(temp.data, end=" ")
                self.preorder(temp.left)
                self.preorder(temp.right)
    
        # Postorder Traversal
        def postorder(self, temp):
            if temp is not None:
                self.postorder(temp.left)
                self.postorder(temp.right)
                print(temp.data, end=" ")
    
        