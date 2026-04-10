class Node:
    def __init__(self,data):
     self.data=data
     self.next=None
class SingleLinkedList:
    def __init__(self):
        self.head=None
    def search(self,key):
        if self.head is None:
            print("list is empty")
            return
        temp=self.head
        pos=1
        while temp:
            if temp.data==key:
                print(f"element is found at position:{pos}")
                return
            temp=temp.next
            pos+=1
        print("elemenet is not in the list")
            

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
l.head.next=n1
n2=Node(30)
n1.next=n2
l.search(30)
l.display()
