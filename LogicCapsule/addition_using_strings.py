def add_strings(str1,str2):
    num1,num2=int(str1),int(str2)
    if num1>=0 and num2>=0:
        sum=num1+num2
    return str(sum)
print(add_strings('134','1234'))