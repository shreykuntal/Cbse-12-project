def PUSH(stack, element):
    stack.append(element)
def POP(stack):
    return stack.pop()
def eval(string):
    print("Expression to evaluate:",string)
    values = string.split(' ')
    s = []
    for i in values:
        if i == "+":
            PUSH(s, float(POP(s))+float(POP(s)))
        elif i == "-":
            PUSH(s, float(POP(s))-float(POP(s)))
        elif i == "*":
            PUSH(s, float(POP(s))*float(POP(s)))
        elif i == "/":
            divisor = float(POP(s))
            dividend = float(POP(s))
            PUSH(s, dividend/divisor)
        else:
            PUSH(s, i)
    return s[0]
string = "10 30 + 50 * 200 - 5 /"
print("Ans:",eval(string))
string = "2 3 + 4 * 5 /"
print("Ans:",eval(string))
