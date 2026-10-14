class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class SCLL:
    def __init__(self):
        self.head=None
    
    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=new_node
        new_node.next=self.head
    
    # def insert(self, new_node, pos):
    #     if pos == 1:  #insert a node at 1st position
    #         temp=self.head
    #         while temp.next!=self.head:
    #             temp=temp.next
    #         temp.next=self.head
    #     else: #insert node from 2nd to last position
    #         p = 1
    #         temp = self.head
    #         while p != pos - 1:
    #             temp = temp.next
    #             p += 1
    #         new_node.next = temp.next
    #         temp.next = new_node

    def insert(self, new_node, pos):  
        if pos == 1:
            temp = self.head
            while temp.next != self.head:
                temp=temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next=self.head
        else:#insert node from 2nd to last position
            p = 1
            temp = self.head
            while (p != pos - 1 and temp.next != self.head):
                temp = temp.next
                p += 1
            new_node.next = temp.next
            temp.next = new_node

    # def delete(self, value):
    #     temp = self.head
    #     prev=None
    #     if temp.data == value:  # Delete the first node
    #         self.head = self.head.next
    #         while temp.next!=self.head: #find last node
    #             temp=temp.next
    #         temp.next=self.head
    #     else:
    #         while temp.data!=value and temp:
    #             prev=temp
    #             temp=temp.next
    #             if temp==self.head:
    #                 print("Value not present in the list")
    #                 return
    #         prev.next=temp.next
            # temp=None

    def delete(self, value):
        if self.head is None:
            print("List is Empty!")
            return
        temp = self.head
        prev = None
        if temp.data == value:  # Delete the first node
            if self.head.next == self.head:
                self.head = None
                return
            self.head = self.head.next
            while temp.next != self.head:  # Find last node
                temp = temp.next
            temp.next = self.head
        else:
            temp = self.head
            while temp.data != value:
                prev = temp
                temp = temp.next
                if temp == self.head:
                    print("Value not present in the list")
                    return
            prev.next = temp.next
            temp = None

    def print(self):
        temp=self.head
        while(True):
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.head:
                break
        print()

list1 = SCLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()
list1.insert(Node(34),1)
list1.print()
list1.insert(Node(50),6)
list1.print()
list1.insert(Node(2),2)
list1.print()
list1.delete(2)
list1.print()
list1.delete(50)
list1.print()
list1.delete(34)
list1.print()