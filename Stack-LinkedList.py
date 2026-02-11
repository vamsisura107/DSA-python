class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self):
        n=int(input("enter the element to be pushed into the stack"))
        new=Node(n)
        if self.top==None:

            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new
    def pop(self):
        if self.top==None:
            print("stack is empty")
        elif self.top.next is None:
            print("popped element is ",self.top.data)
            self.top=None

        else:
            temp=self.top
            print("popped element is ",self.top.data)
            self.top=temp.next
            temp=None
    def display(self):
        if self.top==None:
            print("stack is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next
            print("\ntop of the stack is",self.top.data)
            print("---------------------------------")

s=Stack()
while(1):
    print("enter the option from below\n1-push\n2-pop\n3-display\n4-exit")
    str=input()
    if str=="1":
        print("push operation")
        s.push()
    elif str=="2":
        print("pop operation")
        s.pop()
    elif str=="3":
        print("display operation")
        s.display()
    else:
        print("exit from program")
        break