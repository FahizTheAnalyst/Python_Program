n=int(input("enter the number:"))
print("the factors of",n)
for x in range(1,n+1):
    if n%x==0:
        print(x)
