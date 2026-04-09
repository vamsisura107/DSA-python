class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    def middle(self):
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.data if slow else None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next

l=DoubleLinkedList()

n1=Node(20)
l.head=n1

n2=Node(30)
n2.prev=n1
n1.next=n2

n3=Node(40)
n3.prev=n2
n2.next=n3

print("Doubly Linked List:")
l.display()

print("\nMiddle element:", l.middle())
