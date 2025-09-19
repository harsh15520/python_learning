def add(a,b):
    return calc(a,b,"+")
def sub(a,b):
    return calc(a,b,"-")
def mul(a,b):
    return calc(a,b,"*")
def div(a,b):
    return calc(a,b,"/")
def calc(a,b,op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("Unknown operator")
#userinput
a = int(input("Enter the first number: "))
operation = input("Enter the operation:add,sub,mul,div ")
ops = {"add": add, "sub": sub, "mul": mul, "div": div}
b = int(input("Enter the second number: "))

if operation not in ops:
    print("Invalid operation")
else:
    func=ops[operation](a,b)
    print(func)
