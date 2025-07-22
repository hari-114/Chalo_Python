def add(list):
    x= sum(list)
    return x
print("SUM OF ELEMENTS IN LIST")
list = [1,2,3,4]
print(add(list))

def reverse(str):
    revStr=str[::-1]
    return revStr
print("REVERSE OF STRING")
str="Vikarthan"
print(reverse(str))

def factorial(n):
    result = 1
    while n > 1:
         result = result*n
         n=n-1
    return result
print("FACTORIAL OF THE NUMBER")
print(factorial(3))

def no_UandL(str):
    lC=0
    uC=0
    space=0
    for i in str:
        if i.islower():
            lC+=1
        elif i.isupper():
            uC+=1
        else:
            space+=1
    print(lC)
    print(uC)
    print(space)
print("PRINTING LOWER CASE AND UPPER CASE")
str="Adithya Verma "
no_UandL(str)

def even_num(list):
    even_list=[]
    for i in range(len(list)):
        if list[i]%2==0:
            even_list.append(list[i])
      
    print(even_list)
print("EVEN NUMBERS IN A LIST")
l1=[1,2,3,4,5,6,4,7,9]
even_num(l1)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print("PRIME OR NOT")
print(isPrime(int(input("Enter to check prime or not: "))))
