nums = [2,3,4,5]
target = 6
def twoSum(nums, target):
    numIndex = {}
    for i, num in enumerate(nums):
        extra = target - num
        if extra in numIndex:
            return [numIndex[extra], i]
        numIndex[num] = i
    return []
print(twoSum(nums, target))

'''arr = []
for i in range(5):
    arr.append(int(input("Enter a numbers: ")))

def greatestNum(arr):
    greatest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > greatest:
            greatest = arr[i]
    return greatest
print("The greatest number is:", greatestNum(arr))'''

#sum of digits of a number

n = 12345
def sum_of_digits(n):
    sum =0
    while n > 0:
        if n > 9:
            digit = n % 10
            sum = sum + digit
            n = n//10
    return sum

print("The sum of digits is:", sum_of_digits(n))
