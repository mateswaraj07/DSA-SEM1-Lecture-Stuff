
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

    # Finding Minimum Value
    def minvalue(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp

    # Deletion
    def delete(self, temp, value):
        if temp is None:
            return temp

        if value < temp.data:
            temp.left = self.delete(temp.left, value)

        elif value > temp.data:
            temp.right = self.delete(temp.right, value)

        else:
            # No child
            if temp.left is None and temp.right is None:
                return None

            # Only right child
            elif temp.left is None:
                return temp.right

            # Only left child
            elif temp.right is None:
                return temp.left

            # Two children
            else:
                minnode = self.minvalue(temp.right)
                temp.data = minnode.data
                temp.right = self.delete(temp.right, minnode.data)

        return temp
                
                
# Main Program
tree = BST()

# Inserting nodes
tree.insert(Node(50))
tree.insert(Node(30))
tree.insert(Node(70))
tree.insert(Node(20))
tree.insert(Node(40))
tree.insert(Node(60))
tree.insert(Node(80))

# Display Traversals
print("Inorder:")
tree.inorder(tree.root)

print("\nPreorder:")
tree.preorder(tree.root)

print("\nPostorder:")
tree.postorder(tree.root)

# Deleting a node
tree.root = tree.delete(tree.root, 70)

print("\n\nAfter Deletion (Inorder):")
tree.inorder(tree.root)