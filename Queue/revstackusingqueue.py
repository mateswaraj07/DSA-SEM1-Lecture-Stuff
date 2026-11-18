# # W.A.P to reverse stack elements using queue.
# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None
# class Stack:
#     def __init__(self):
#         self.top=None
#     def push(self, new_node):
#         new_node.next=self.top
#         self.top=new_node
#     def pop(self):
#         if self.top is None:
#             return None
#         temp=self.top
#         self.top=self.top.next
#         return temp.data
#     def print(self):
#         temp=self.top
#         print("Stack Elements:")
#         while temp:
#             print(temp.data, end=" -> ")
#             temp=temp.next
#         print("None")
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#     def is_empty(self):
#         return self.front is None
#     def enqueue(self, data):
#         new = Node(data)
#         if self.rear is None:
#             self.front = self.rear = new
#         else:
#             self.rear.next = new
#             self.rear = new
#     def dequeue(self):
#         if self.front:
#             temp=self.front
#             data=temp.data
#             self.front=self.front.next
#             if self.front is None:
#                 self.rear=None
#             return data
#         else:
#             return None
#     def print_queue(self):
#         curr=self.front
#         print("Queue Elements:")
#         while curr is not None:
#             print(curr.data, end=" -> ")
#             curr=curr.next
#         print("None")
# def reverse_stack(st1):
#     q1=Queue()
#     # Transfer Stack to Queue
#     while st1.top is not None:
#         q1.enqueue(st1.pop())
#     q1.print_queue()
#     # Transfer Queue back to Stack
#     while not q1.is_empty():
#         st1.push(Node(q1.dequeue()))
# # Main program
# st=Stack()
# st.push(Node(10))
# st.push(Node(20))
# st.push(Node(30))
# st.push(Node(40))
# print("Original Stack:")
# st.print()
# reverse_stack(st)
# print("\nReversed Stack:")
# st.print()

#Reverse Stack-Queue
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node  
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            popped_data=temp.data  
            self.top=self.top.next
            temp=None
            return popped_data
    
    def print(self):
        temp=self.top
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def isempty(self):
        return self.front is None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        dequed_data=temp.data
        self.front=self.front.next
        if self.front ==None: #if there is only one node
            print("Queue is empty now")
            self.rear=None
        temp=None
        return dequed_data
    def print(self):
        temp=self.front
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print()

def reverse_stack(s1):
    print("Reverse Stack using Queue")
    q1=LQueue()
    while not s1.isempty(): #pop from stack and enqueue to queue
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    print("Stack is reversed...")
    s1.print()
def reverse_queue(q1):
    print("Reverse Queue using Stack")
    s2=stack()
    while not q1.isempty():
        s2.push(Node(q1.dequeue()))
    while not s2.isempty(): #pop from stack and enqueue to queue
            q1.enqueue(Node(s2.pop()))
    print("Queue is reversed...")
    q1.print()

st=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
reverse_stack(st)
que=LQueue()
que.enqueue(Node(25))
que.enqueue(Node(35))
que.enqueue(Node(45))
que.enqueue(Node(55))
que.print()
reverse_queue(que)