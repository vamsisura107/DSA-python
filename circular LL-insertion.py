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
    def insert_begining(self,x):
        n=Node(x)
        if self.head is None:
            self.head=n
            self.tail=n
            self.tail.next=self.head
        else:
            n.next=self.head
            self.tail.next=n
            self.head=n
    def insert_end(self,x):
        n=Node(x)
        if self.head is None:
            self.head=n
            self.tail=n
            self.tail.next=self.head
        else:
            self.tail.next=n
            self.tail=n
            self.tail.next=self.head
    def insert_pos(self,pos,x):
        n=Node(x)
        if self.head is None:
            self.head=n
            self.tail=n
            self.tail.next=self.head
        else:
            if pos==1:
                l.insert_begining(x)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                n.next=temp.next
                temp.next=n




l=CLL()
l.insert_begining(1)
l.display()
l.insert_begining(2)
l.display()
l.insert_end(3)
l.display()
l.insert_pos(4,4)
l.display()