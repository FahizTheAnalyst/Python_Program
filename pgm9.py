def replace_char(str):
    return str[-1]+str[1:-1]+str[0]
str=input("enter the word:")
s=replace_char(str)
print(s)

