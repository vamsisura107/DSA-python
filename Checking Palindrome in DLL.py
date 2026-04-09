class Node:
    def __init__(self,data):
     self.data=data
     self.next=None
     self.prev=None
class doubleLinkedList:
    def __init__(self):
        self.head=None
    def is_palindrome(self):
        right=self.head
        left=self.head
        while right.next:
            right=right.next
        while left!=right and left.prev !=right:
            if left.data!=right.data: 
               print("Not a Palindrome")
               return
            left=left.next
            right=right.prev
        print("Palindrome")
    def display(self):
        if self.head is None:
            print("empty List")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
l=doubleLinkedList()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n2.prev=n1
n3=Node(20)
n3.prev=n2
n2.next=n3
n4=Node(10)
n3.next=n4
n4.prev=n3
l.is_palindrome()
l.display()

