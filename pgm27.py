string=input("enter string:")
if string[-3:]=='ing':
    string+='/y'
else:
    string+='ing'
    print(string)