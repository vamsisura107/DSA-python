class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        temp=None
        current=self.head
        while current:
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        if temp:
            self.head=temp.prev 
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
print("dublelinkedlist befor reversed:")
l.display()
print()
print("after reversed:")
l.reverse()
l.display()
