class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # 1. Append a node
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    # 2. Insert a node at a specific position
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        p = 1

        while p < pos - 1 and temp:
            temp = temp.next
            p += 1

        if temp == None:
            print("Invalid position")
            return

        new_node.prev = temp
        new_node.next = temp.next

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # 3. Delete a node by value
    def delete(self, value):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        # Delete the first node
        if temp.data == value:
            self.head = temp.next

            if self.head:
                self.head.prev = None

            return

        # Find the node
        while temp and temp.data != value:
            temp = temp.next

        if temp == None:
            print("Value not found")
            return

        # Connect the previous and next nodes
        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # 4. Delete a node at a specific position
    def delete_pos(self, pos):
        if pos < 1 or self.head == None:
            print("Invalid position or empty list")
            return

        temp = self.head

        if pos == 1:
            self.head = temp.next

            if self.head:
                self.head.prev = None

            return

        p = 1

        while p < pos and temp:
            temp = temp.next
            p += 1

        if temp == None:
            print("Invalid position")
            return

        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # 5. Delete the first node
    def del_first(self):
        if self.head == None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # 6. Delete the last node
    def del_last(self):
        if self.head == None:
            print("List is empty")
            return

        temp = self.head

        # Only one node
        if temp.next == None:
            self.head = None
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # 7. Reverse the doubly linked list
    def reverse(self):
        temp = self.head
        prev = None

        while temp:
            prev = temp.prev
            temp.prev = temp.next
            temp.next = prev
            temp = temp.prev

        if prev:
            self.head = prev.prev

    # 8. Find the middle node
    def find_mid(self):
        if self.head == None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle Node:", slow.data)

    # 9. Find and delete the middle node
    def findmid_del(self):
        if self.head == None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Deleted Middle Node:", slow.data)

        if slow.prev:
            slow.prev.next = slow.next
        else:
            self.head = slow.next

        if slow.next:
            slow.next.prev = slow.prev

    # 10. Print the list forward
    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()

    # 11. Print the list backward
    def print_reverse(self):
        temp = self.head

        if temp == None:
            print("List is empty")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" ")
            temp = temp.prev

        print()


# Create the doubly linked list
list1 = DLL()

list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))

print("Original List:")
list1.print()

print("Insert 34 at position 1:")
list1.insert(Node(34), 1)
list1.print()

print("Insert 60 at position 6:")
list1.insert(Node(60), 6)
list1.print()

print("Delete value 30:")
list1.delete(30)
list1.print()

print("Delete node at position 2:")
list1.delete_pos(2)
list1.print()

print("Delete first node:")
list1.del_first()
list1.print()

print("Delete last node:")
list1.del_last()
list1.print()

print("Middle node:")
list1.find_mid()

print("Forward traversal:")
list1.print()

print("Backward traversal:")
list1.print_reverse()

print("Reverse the list:")
list1.reverse()
list1.print()

print("Find and delete the middle node:")
list1.findmid_del()
list1.print()