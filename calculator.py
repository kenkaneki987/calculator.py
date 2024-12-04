def calculator(n1,n2,op):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="^":
        return n1**n2
    elif op=="/":
        return n1/n2
    elif op=="//":
        return n1//n2
    else:
        print("use a valid opertor")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
op=input("which operator do u wanna use:")
a=calculator(n1,n2,op)
print(a)

