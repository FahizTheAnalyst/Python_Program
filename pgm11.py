a=int(input("enter first number:"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    print(a,"is the biggest number")
elif b>c:
    print(b,"is the biggest number")
else:
    print(c,"is the biggest number")