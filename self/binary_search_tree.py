
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
    def minimumvalue(self, temp):
        while temp.left is not None:
            temp = temp.left
        return temp.data
    
    # Helper Function for delete()
    def minvalue(self, temp):
            while temp.left is not None:
                temp = temp.left
            return temp
    
    # Finding Maximum Value
    def maxvalue(self, temp):
        while temp.right is not None:
            temp=temp.right
        return temp.data
    
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
    
    # Descending order
    def descending(self, temp):
        if temp is not None:
            self.descending(temp.right)
            print(temp.data, end=" ")
            self.descending(temp.left)

    # Count siblings of a particular node
    def siblings(self, temp, value):
        if temp is None:
            return 0
        if temp.left is not None and temp.right is not None:
            if temp.left.data == value or temp.right.data == value:
                return 1
        return (self.siblings(temp.left, value) +
                self.siblings(temp.right, value))
    
    # inorder and preorder is given and told to construct a tree from it
    def build_pre_in(self, inorder, preorder):
        if len(inorder) == 0:
            return None
        root = Node(preorder[0])
        pos = inorder.index(preorder[0])
        root.left = self.build_pre_in(
            inorder[:pos], preorder[1:pos+1])
        root.right = self.build_pre_in(
            inorder[pos+1:], preorder[pos+1:])
        return root

    #inorder and postorder is given and told to construct a tree from it
    def build_post_in(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        root = Node(postorder[-1])
        pos = inorder.index(postorder[-1])
        root.left = self.build_post_in(
            inorder[:pos], postorder[:pos])
        root.right = self.build_post_in(
            inorder[pos+1:], postorder[pos:-1])
        return root
        
# Main Program
tree = BST()
tree1 = BST()
tree2 = BST()

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
tree.root = tree.delete(tree.root, 70) # Update root with the modified BST after deletion

print("\n\nAfter Deletion (Inorder):")
tree.inorder(tree.root)

#Descending Order
print("\n\nDescending Order using Inorder")
tree.descending(tree.root)

# Minimum Value
print("\n\nMinimum Value: ",tree.minimumvalue(tree.root))

# Maximum Value
print("\n\nMaximum Value: ",tree.maxvalue(tree.root))

# Inorder + Preorder Construction
print("\n\nConstructing Tree using Inorder + Preorder")
inorder1 = [20, 30, 40, 50, 60, 70, 80]
preorder1 = [50, 30, 20, 40, 70, 60, 80]
print("Given Inorder:", inorder1)
print("Given Preorder:", preorder1)
tree1.root = tree1.build_pre_in(inorder1, preorder1)
print("Inorder:")
tree1.inorder(tree1.root)
print("\nPreorder:")
tree1.preorder(tree1.root)
print("\nPostorder:")
tree1.postorder(tree1.root)

# Inorder + Postorder Construction
print("\n\nConstructing Tree using Inorder + Postorder")
inorder2 = [20, 30, 40, 50, 60, 70, 80]
postorder2 = [20, 40, 30, 60, 80, 70, 50]
print("Given Inorder:", inorder2)
print("Given Postorder:", postorder2)
tree2.root = tree2.build_post_in(inorder2, postorder2)
print("Inorder:")
tree2.inorder(tree2.root)
print("\nPreorder:")
tree2.preorder(tree2.root)
print("\nPostorder:")
tree2.postorder(tree2.root)