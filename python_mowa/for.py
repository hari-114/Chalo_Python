for i in range(1,11):
    print(i, end='\t')

print("\n-------------------------------------------------------------")

for i in range(23,57):
    if i % 2 == 0:
        print(i,end = ' ')

print("\n-------------------------------------------------------------")

num = int(input("Enter a number to check if it is prime: "))
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(isPrime(num))

print("-------------------------------------------------------------")  

print("print prime numbers from 10 to 99")
for num in range(10, 100):
    if isPrime(num):
        print(num, end=' ')
    
