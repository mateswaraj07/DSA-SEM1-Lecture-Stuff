class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Adding node at beginning.")
head=n1
new=Node(50)
new.next=head
head=new
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Deleting at beginning.")
if head is not None:
  head=head.next
  curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Deleting at last.")
curr=head
while curr.next.next is not None:
  curr=curr.next
curr.next=None
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Deleting a particular node.")
curr=head
while curr.next.data != 30:
  curr=curr.next
curr.next=curr.next.next
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Inserting at last.")
new=Node(60)
head=n1
curr=head
while curr.next is not None:
  curr=curr.next
curr.next=new
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()
print("Inserting at 3rd position.")
new=Node(25)
curr=n1
while curr is not None and curr.data!=20:
  curr=curr.next
new.next=curr.next
curr.next=new
curr=head
while curr is not None:
  print(curr.data, end=" -> ")
  curr=curr.next
print("None")
print()