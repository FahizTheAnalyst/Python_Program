def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
result=gcd(a,b)
print(f"the gcd of {a}and {b} is {result}")
