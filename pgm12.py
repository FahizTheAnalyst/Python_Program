name=input("enter the file name:")
if'.'in name:
    extension=name.split('.')
    print(extension[-1])
else:
    print("the file has no extension")