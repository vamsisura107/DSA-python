class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head==None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
l=singlelinkedlist()
n=Node(10)
l.head=n
n1=Node(20)
l.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
print("linked list")
l.display()
middle=l.find_middle()
print(f"middle element:{middle}")
