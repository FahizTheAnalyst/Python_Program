a=int(input("enter the start year"))
b=int(input("enter the end year"))
for i in range(a,b+1):
    if(i%4==0 and i%100!=0 or i%4==0):
         print(i)