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
def PEEK(stack):
    if isStackEmpty(stack):
        return "Underflow"
    return stack[-1]
def DISPLAY(stack):
    if isStackEmpty(stack):
        print "Stack is Empty"
        return None
    print(stack[-1],"- TOP")
    for i in range(len(stack)-2,-1,-1):
        print(stack[i])
def MAIN_MENU(stack):
    while True:
        print("Stack Implementation")
        print("1 - Push")
        print("2 - Pop")
        print("3 - Peek")
        print("4 - Display")
        print("5 - Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            el = int(input("Enter value to push: "))
            PUSH(stack, el)
        elif ch == 2:
            print(POP(stack))
        elif ch == 3:
            print(PEEK(stack))
        elif ch == 4:
            print(DISPLAY(stack))
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid Input")
s = []
MAIN_MENU(s)
