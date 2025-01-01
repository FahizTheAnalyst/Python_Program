l1=[]
n=int(input("enter a limit:"))
for i in range(n):
    val=int(input("enter the values:"))
    l1.append(val)
    numbers=[x for x in l1 if x% 2!=0]
print(numbers)