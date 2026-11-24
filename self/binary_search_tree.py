
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

    