class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubleLinkedList:
    def __init__(self):
       self.head=None
    def search(self, key):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        pos = 1
        while temp:   # same as singly
            if temp.data == key:
                print(f"Element found at position {pos}")
                return
            temp = temp.next
            pos += 1
        print("Element is not in the list")
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=doubleLinkedList()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(30)
n3.prev=n2
n2.next=n3
l.search(30)
l.display()
