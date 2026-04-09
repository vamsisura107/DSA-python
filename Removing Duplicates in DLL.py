class Node:
    def __init__(self,data):
     self.data=data
     self.next=None
     self.prev=None
class doubleLinkedList:
    def __init__(self):
        self.head=None
    def remove_duplicates(self):
        temp=self.head
        while temp:
            runner=temp.next
            while runner:
                next_node=runner.next
                if temp.data == runner.data:
                    runner.prev.next=runner.next
                    if runner.next:
                        runner.next.prev=runner.prev
                runner = next_node
            temp=temp.next
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
n4=Node(30)
n3.next=n4
n4.prev=n3
l.display()
print()
print("After Removing Duplicates:")
l.remove_duplicates()
l.display()
