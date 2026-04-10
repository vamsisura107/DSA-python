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
    def deleteb(self):
        if self.head is None:
            print("linked list is empty")
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
    def delete(self):
        if self.head is None:
            print("linked list is empty")
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
    def deletep(self,pos):
        if self.head is None:
            print("list is empty")
        elif pos==1:
            self.deleteb()
        else:
            temp=self.head
            for i in range(1,pos-1):
                temp=temp.next
            need_to_remove=temp.next
            temp.next=need_to_remove.next
            if need_to_remove==self.tail:
                self.tail=temp
        
l=CLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
n3.next=l.head
l.tail=n3
l.display()
l.deletep(2)
l.display()
