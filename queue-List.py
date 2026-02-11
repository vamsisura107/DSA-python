def enqueue():
    n=input("enter the element to be inserted")
    queue.append(n)
    print("  ")
def dequeue():
    if (len(queue)==0):
        print("the queue is empty")
        print()
    else:
        print(queue[0],"is the elements deleted from the queue ")
        del queue[0]
        print("  ")
def display():
    if len(queue)==0:
        print("the queue is empty")
    else:
        for ele in queue:
            print(ele,end=" ")
        print("front element of the queue is ",queue[0])
        print("rear element of the queue is ",queue[-1])
        print()
queue=list()
while(1):
    print("enter the option from below\n1-enqueue\n2-dequeue\n3-display\n4-exit")
    str = input()
    if str == "1":
        print("enqueue operation")
        enqueue()
    elif str == "2":
        print("dequeue operation")
        dequeue()
    elif str == "3":
        print("display operation")
        display()
    else:
        print("exit from program")
        break