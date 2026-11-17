# W.A.P to to reverse a queue using stack.
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node
    def print(self):
        temp=self.top
        print("Stack Elements:")
        while temp:
            print(temp.data)
            temp=temp.next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
    def dequeue(self):
        if self.front:
            temp=self.front
            dequeued_data=temp.data
            self.front=self.front.next
            if self.front is None:
                self.rear = None
                print("Queue is empty")
            temp=None
            return dequeued_data
        else:
            print("Queue is empty")
        
    def print_queue(self):
        curr = self.front

        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next

        print("None")

def reverse_queue(q1):
    st1=Stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
    st1.print()

# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Queue:")
q.print_queue()

reverse_queue(q)