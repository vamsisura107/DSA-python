class Node:
    def __init__(self,data):
     self.data=data
     self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insertion_at_beginning(self,data):
        ib=Node(data)
        ib.next=self.head
        self.head=ib
    def insertion_at_end(self,data):
        ie=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ie
    def insertion_at_position(self,pos,data):
        ip=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        ip.data=data
        ip.next=temp.next
        temp.next=ip

    def display(self):
        if self.head is None:
            print("empty List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=SingleLinkedList()
n=Node(10)
l.head=n
n1=Node(20)
l.next=n1
n2=Node(30)
n1.next=n2
l.insertion_at_beginning(5)
l.insertion_at_end(40)
l.insertion_at_position(3,25)
l.display()

