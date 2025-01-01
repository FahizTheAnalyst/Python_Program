n=int(input("enter the limit:"))
fib=[0,1]
if n==1:
    print([0])
elif n==2:
    print(fib)
else:
    for x in range(2,n):
        c=fib[-1]+fib[-2]
        fib.append(c)
        print(fib)