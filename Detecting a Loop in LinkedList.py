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
    def detect_loop(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        
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
print("Does loop exist initially?",l.detect_loop())
n3.next=n1
print("Does loop exist after creating cycle?",l.detect_loop())

    
        
