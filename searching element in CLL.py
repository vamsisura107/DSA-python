class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("circular linked list is empty")
        else:
            temp=self.head
            print(temp.data,"--",end=" ")
            while temp.next != self.head:
                temp=temp.next
                print(temp.data,"--",end=" ")
            print(temp.next.data)

    def search(self, key):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        pos = 1
        while True:
            if temp.data == key:
                print(f"Element found at position {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        print("Element is not in the list")
l=CLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
n3.next=l.head
l.tail=n3
l.search(30)
l.display()
