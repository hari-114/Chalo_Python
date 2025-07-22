import sys
n = len(sys.argv)

print("name of The file:",sys.argv[0])
print("Total arguments Passed: ",n)

print(sys.argv[9])

# sum = 0
# for i in range(1,n):
#     sum += int(sys.argv[i])

# print("Result: ",sum)
# print("name of The file:",sys.argv[0])
# print(sys.argv[1:])
# args=sys.argv[1:]
# if all(arg.isdigit() for arg in args): 
#         numbers = [int(arg) for arg in args]

# print(numbers)

# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# sum =0

# for num in numbers:
#     if isPrime(num):
#         sum += num
#     else:
#         continue
# print(sum)

#Mini project
# n = len(sys.argv)
# print(n)
# print(sys.argv)

# str1=sys.argv[1].split('-')
# str2=sys.argv[2].split('-')
# str3=sys.argv[3].split('-')
# print(str1,str2,str3)
# happiness=0
# for num in str3:
#     if num in str1:
#         happiness+=1
#     elif num in str2:
#         happiness-=1

# print(happiness)