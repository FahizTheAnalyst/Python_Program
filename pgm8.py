def replace_char(str):
    char=str[0]
    str=str.replace(char,'$')
    str=char+str[1:]
    return str
str=input("enter the string:")
s=replace_char(str)
print(s)