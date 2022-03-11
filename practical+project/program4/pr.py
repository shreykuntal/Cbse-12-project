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
def MENU(stack):
    while True:
        print("1 - ADD City")
        print("2 - POP City")
        print("3 - Exit")
        ch=int(input("Enter your choice:"))
        if ch == 1:
            to_push = []
            pincode = int(input("Enter pincode: "))
            name = input("Enter city name: ")
            to_push.append(pincode)
            to_push.append(name)
            PUSH(stack, to_push)
        elif ch == 2:
            if isStackEmpty(stack):
                return "Underflow"
            POP(stack)
        elif ch == 3:
            print("Exiting..")
            break
        else:
            print("Invalid Input")
s = []
MENU(s)
