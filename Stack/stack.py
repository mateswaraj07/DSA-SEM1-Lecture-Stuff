# stack using linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        temp=self.top
        print("Popped Element: ", temp.data)
        self.top=self.top.next
        temp=None

    def print(self):
        temp=self.top
        print("Stack Elements:")
        while temp:
            print(temp.data)
            temp=temp.next

s = Stack()
s.push(Node(10))
s.push(Node(20))
s.push(Node(30))
s.push(Node(40))
s.push(Node(50))
s.print()
s.pop()
s.print()