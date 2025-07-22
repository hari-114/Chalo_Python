a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
try:
    c=a/b
    print(int(c))
except Exception as e:
      print("Error Occured: ",e)
else:
      print("Division Successful")
finally:
      print("execution Completed")

def isPrime(n):
        if n <=1:
            return False
        for i in range(2,n):
            if n%i==0:
                  return False
        return True

try:
    num = int(input("Enter to know given NUmber is prime or not: "))
    print(isPrime(num))
except ValueError:
    print('Enter a valid Number')
        
import os
try:
    f1=input('Enter file name to open: ')
    result = os.path.exists('c:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\'+f1)
    # print(result)
    f2=open('c:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\'+f1,'r')
    print(f2.read())
except FileNotFoundError:
     print('Error : File not found')

l1=[1,'Hari',90,90,80,9.09]
try:
     index=int(input("Enter Index to find: "))
     print(l1[index])
except IndexError:
     print("Invalid index")