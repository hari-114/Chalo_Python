#n = 12345
def sum_of_digits(n):
    sum = 0
    while n > 0:
                digit = n % 10
                sum = sum + digit
                n = n//10
                if sum > 9:
                    sum = sum_of_digits(sum)
    if sum < 10:
           return sum

#reverse a number
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

#check if a number is palindrome
def is_palindrome(n):
    original = n
    reversed_num = reverse_number(n)
    return original == reversed_num

#factorial of a number
def factorial(n):
    result = 1
    while n > 1:
         result = result*n
         n=n-1
    return result