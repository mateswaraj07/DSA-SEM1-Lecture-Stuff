class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    # Insert a new node
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right
    # Inorder: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    # Preorder: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    # Postorder: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
# Main Program
bst = BST()
# Insert elements
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
# Display traversals
print("Inorder Traversal:")
bst.inorder(bst.root)
print("\nPreorder Traversal:")
bst.preorder(bst.root)
print("\nPostorder Traversal:")
bst.postorder(bst.root)