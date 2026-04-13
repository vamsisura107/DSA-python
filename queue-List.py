def enqueue():
    n = input("enter the element to be inserted: ")
    queue.append(n)
    print("Element added.")
def dequeue():
    if len(queue) == 0:
        print("queue is empty")
    else:
        # Fixed: Changed dequeue[0] to queue[0]
        print(queue[0], "is the element deleted from queue")
        del queue[0]
        print(" ")
def display():
    if len(queue) == 0:
        print("list is empty")
    else:
        print("Queue elements:", end=" ")
        for ele in queue:
            print(ele, end=" ")
        print("\nfront of the queue is:", queue[0])
        print("rear of the queue is:", queue[-1])

queue = list()
while True:
    print("\nenter the option from below\n1-enqueue\n2-dequeue\n3-display\n4-exit")
    choice = input("Choice: ")
    if choice == "1":
        print("--- enqueue operation ---")
        enqueue()
    elif choice == "2":
        print("--- dequeue operation ---")
        dequeue()
    elif choice == "3":
        print("--- display operation ---")
        display()
    elif choice == "4":
        print("exit from the program")
        break
    else:
        print("Invalid option, please try again.")
