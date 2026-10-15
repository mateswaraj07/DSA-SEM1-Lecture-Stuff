# Create a Singly Linear Linked List with following operations
# 1. Create Linked List (append)
# 2. Traverse and print the node values
# 3. Insert node at a specific position
# 4. Delete alternate nodes in the linked list
class Node:
    def _init_(self, data):
        self.data=data
        self.next=None
class SLL:
    def _init_(self):
        self.head=None

    #Append
    def append(self, data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=new

    #Insert
    def insert(self, data, pos):
        new=Node(data)
        if pos<0:
            print("Invalid Position")
            return
        if pos==0:
            new.next=self.head
            self.head=new
            return
        temp=self.head
        for i in range(pos-1):
            if temp==None:
                print("Invalid Position")
                return
            temp=temp.next
        if temp==None:
            print("Invalid Position")
            return
        new.next=temp.next
        temp.next=new

    #Traverse
    def display(self):
        temp=self.head
        if temp==None:
            print("List is empty")
            return
        while temp!=None:
            print(temp.data, end=" -> ")
            temp=temp.next
        print("None")

    #Delete Alternate
    def del_alternate(self):
        temp=self.head
        while temp and temp.next:
            temp.next=temp.next.next
            temp=temp.next

ll=SLL()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print("\nOriginal List:")
ll.display()
print()
print("Insering at 6th position")
ll.insert(60,5)
ll.display()
print()
print("After deleting alternate nodes:")
ll.del_alternate()
ll.display()