class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubleLinkedList:
    def __init__(self):
       self.head=None
    def insert_beg(self,data):
        n=Node(data)
        temp=self.head
        n.next=temp
        temp.prev=n
        self.head=n
    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        n.prev=temp
        temp.next=n
    def insert_position(self,data,pos):
        n=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.next=temp.next
        n.prev=temp
        temp.next.prev=n
        temp.next=n

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
l.insert_beg(5)
l.insert_end(40)
l.insert_position(25,4)
l.display()
