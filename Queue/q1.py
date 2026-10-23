# circular queue
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
        self.rear.next=self.front #added for circular

    # def dequeue(self):
    #     if self.front:
    #         temp = self.front
    #         self.front = self.front.next
    #         if self.front==self.rear: #updated for circular q
    #             self.rear = None
    #             print("now queue is empty")
    #             return
    #         temp=None
    #         self.rear.next=self.front #added for circular q
    #     else:
    #         print("Queue is empty")


    def dequeue(self):
        if self.front:
            temp = self.front

            if self.front == self.rear:  # Only one element
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.rear.next = self.front

            print("Deleted:", temp.data)
            temp = None

        else:
            print("Queue is empty")


    # def print(self):
    #     temp = self.front

    #     while True:
    #         print(temp.data, end="  ")
    #         temp = temp.next
    #         if temp==self.front:
    #             break

    #     print()
    def print(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        while True:
            print(temp.data, end="  ")
            temp = temp.next

            if temp == self.front:
                break

        print()


q = Queue()

q.enqueue(Node(15))
q.enqueue(Node(25))
q.enqueue(Node(30))
q.enqueue(Node(45))
q.enqueue(Node(40))

print("Queue elements:")
q.print()

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

print("Queue after dequeue:")
q.print()