class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def delete_pos(self,pos):
        before=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            before=before.next
            temp=temp.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
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
l.delete_begining()
l.delete_end()
l.delete_pos(2)
l.display()
