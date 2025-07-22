#write a program to check if a number is positive, negative or zero

num = int(input("Enter a number: "))
if num >0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

#given num is even or odd
print("-------------------------------------------------------------")
number = int(input("Enter a number to check even or odd: "))
if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("-------------------------------------------------------------")
print("Check if last digit of two numbers is same")
def lastDigit(num1, num2):
    if num1 % 10 == num2 % 10:
        return True
    else:
        return False
    
print(lastDigit(int(input("Enter first number: ")), int(input("Enter second number: "))))

