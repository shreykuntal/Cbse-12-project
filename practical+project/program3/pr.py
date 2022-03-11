def PUSH(stack, element):
    stack.append(element)
def POP(stack):
    return stack.pop()
def isPalindrome(string):
    s = []
    if len(string) % 2 != 0:
        mid = (len(string) // 2) + 1
        midN = mid - 1
    else:
        mid = len(string) // 2
        midN = mid
    for i in range(mid , len(string)):
        PUSH(s, string[i])
    for j in range(0, midN):
        if POP(s) != string[j]:
            return False
    return True
string = input("Enter string to check: ")
if isPalindrome(string):
        print("Yes, the string is a palindrome")
else:
        print("No, the string is not a palindrome")

        
