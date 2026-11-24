
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push an element
    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    # Pop an element
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        print("Popped:", self.top.data)
        self.top = self.top.next

    # Display top element
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Check whether stack is empty
    def is_empty(self):
        return self.top is None

    # Count total elements
    def size(self):
        count = 0
        curr = self.top

        while curr is not None:
            count += 1
            curr = curr.next

        print("Stack size:", count)

    # Search for an element
    def search(self, data):
        curr = self.top
        position = 1

        while curr is not None:
            if curr.data == data:
                print("Element found at position:", position)
                return

            curr = curr.next
            position += 1

        print("Element not found")

    # Display bottom element
    def get_bottom(self):
        if self.top is None:
            print("Stack is empty")
            return

        curr = self.top

        while curr.next is not None:
            curr = curr.next

        print("Bottom element:", curr.data)

    # Remove all elements
    def clear(self):
        self.top = None
        print("Stack cleared")

    # Display stack elements
    def display(self):
        curr = self.top

        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("None")

    # Reverse the stack using another stack
    def reverse(self):
        temp = Stack()

        while self.top is not None:
            data = self.top.data
            self.pop_node()
            temp.push(data)

        self.top = temp.top

    # Remove top node without printing
    def pop_node(self):
        if self.top is not None:
            self.top = self.top.next

    def reverse_without_stack(self):
        prev = None
        curr = self.top

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.top = prev

    def largest_smallest(self):
        if self.top is None:
            print("Stack is empty")
            return

        largest = self.top.data
        smallest = self.top.data

        curr = self.top

        while curr is not None:
            if curr.data > largest:
                largest = curr.data

            if curr.data < smallest:
                smallest = curr.data

            curr = curr.next

        print("Largest:", largest)
        print("Smallest:", smallest)

    def copy_stack(self):
        temp = Stack()
        result = Stack()

        curr = self.top

        while curr is not None:
            temp.push(curr.data)
            curr = curr.next

        curr = temp.top

        while curr is not None:
            result.push(curr.data)
            curr = curr.next

        return result

    def insert_bottom(self, data):
        new = Node(data)

        if self.top is None:
            self.top = new
            return

        curr = self.top

        while curr.next is not None:
            curr = curr.next

        curr.next = new

    def sort_stack(self):
        if self.top is None:
            return

        curr = self.top

        while curr is not None:
            temp = curr.next

            while temp is not None:
                if curr.data > temp.data:
                    curr.data, temp.data = temp.data, curr.data

                temp = temp.next

            curr = curr.next

        print("Stack sorted")

# Main program

s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print("Original Stack:")
s.display()

# 1. Peek
print("\n1. Peek:")
s.peek()

# 2. Pop
print("\n2. Pop:")
s.pop()
s.display()

# 3. Check empty
print("\n3. Is Empty:")
print(s.is_empty())

# 4. Size
print("\n4. Size:")
s.size()

# 5. Search
print("\n5. Search:")
s.search(20)

# 6. Bottom element
print("\n6. Bottom Element:")
s.get_bottom()

# 7. Reverse using another stack
print("\n7. Reverse using another stack:")
s.reverse()
s.display()

# 8. Reverse without another stack
print("\n8. Reverse without another stack:")
s.reverse_without_stack()
s.display()

# 9. Largest and smallest
print("\n9. Largest and Smallest:")
s.largest_smallest()

# 10. Copy stack
print("\n10. Copy Stack:")
copy = s.copy_stack()
copy.display()

# 11. Insert at bottom
print("\n11. Insert at Bottom:")
s.insert_bottom(5)
s.display()

# 12. Sort stack
print("\n12. Sort Stack:")
s.sort_stack()
s.display()

# 13. Clear stack
print("\n13. Clear Stack:")
s.clear()
s.display()

print("\nIs Empty:", s.is_empty())
