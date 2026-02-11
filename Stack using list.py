def push():
    n=int(input("enter the number to be pushed"))
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)
        print("n is pushed")
    print()
def pop():
    if len(stack)==0:
        print("stack is empty")
    else:
        print(stack[0],"is deleted from the stack")
        del stack[0]
    print()
def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("elements of the stack are")
        for ele in stack:
            print(ele)
        print("top element of the stack is",stack[0])
        print()
stack=list()
while(1):
    print("enter the option from below\n1-push\n2-pop\n3-display\n4-exit")
    str=input()
    if str=="1":
        print("push operation")
        push()
    elif str=="2":
        print("pop operation")
        pop()
    elif str=="3":
        print("display operation")
        display()
    else:
        print("exit from program")
        break