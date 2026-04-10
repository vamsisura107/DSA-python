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
    def count(self):
        if self.head is None:
            return 0
        count=1
        temp=self.head
        while temp.next!=self.head:
            count+=1
            temp=temp.next
        print("no:of nodes:",count)
           



l=CLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
n3.next=l.head
l.display()
l.count()
