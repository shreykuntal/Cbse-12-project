def isStackEmpty(stack):
    if len(stack) == 0:
        return True
    return False
def PUSH(stack, element):
    stack.append(element)
def POP(stack):
    if isStackEmpty(stack):
        return "Underflow"
    return stack.pop()
def DISPLAY(stack):
    if isStackEmpty(stack):
        print("Stack is Empty")
        return None
    print(stack[-1],"<- TOP")
    for i in range(len(stack)-2,-1,-1):
        print(stack[i])
def MENU(stack):
    while True:
        print("1 - Push")
        print("2 - Pop")
        print("3 - Display")
        print("4 - Exit")
        ch=int(input("Enter your choice:"))
        if ch == 1:
            to_push = []
            empno = int(input("Enter employee number: "))
            name = input("Enter employee name: ")
            salary = input("Enter salary: ")
            to_push.append(empno)
            to_push.append(name)
            to_push.append(salary)
            PUSH(stack, to_push)
        elif ch == 2:
            if isStackEmpty(stack):
                return "Underflow"
            POP(stack)
        elif ch == 3:
            DISPLAY(stack)
        elif ch == 4:
            print("Exiting..")
            break
        else:
            print("Invalid Input")
s = []
MENU(s)
