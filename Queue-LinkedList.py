class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self):
        n=int(input("enter the element to be enqueued "))
        new=Node(n)
        if self.front is None:
            self.front=new
            self.rear=new
        else:
            self.rear.next=new
            self.rear=new
    def dequeue(self):
        if self.front is None:
            print("the queue is empty")
        elif self.front.next is None:
            print("popped element",self.front.data)
            self.front=None
        else:
            temp=self.front
            print("popped element",self.front.data)
            self.front=self.front.next
            self.front=temp.next
            temp=None
    def display(self):
        if self.front is None:
            print("the queue is empty")
        else:
            print("elements of the queue are ")
            temp=self.front
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
            print("\nfront of the queue is ",self.front.data)
            print("rear of the queue is ",self.rear.data)

q=Queue()
while(1):
    print("enter the option from below\n1-enqueue\n2-dequeue\n3-display\n4-exit")
    str = input()
    if str == "1":
        print("enqueue operation")
        q.enqueue()
    elif str == "2":
        print("dequeue operation")
        q.dequeue()
    elif str == "3":
        print("display operation")
        q.display()
    else:
        print("exit from program")
        break