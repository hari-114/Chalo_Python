# dic={}
# for i in range(65,91):
#     dic[chr(i)]=i-ord('A')+1
# print(dic)

# cubes={}
# list1=[1,2,3,4,5,6,7]
# for ele in list1:
#     if ele%2!=0:
#         cubes[ele]=ele**3
n = 582109
print('sums of powers of digits')
def sum_dig(num):
    sum=0
    pow=0
    while num>0:
        digit=num%10
        sum+=digit**pow
        pow=num%10
        num//=10
    return sum
print(sum_dig(n))
def sum_dig_for(num):
    total = 0
    # Reverse the string so that index 0 is the least significant digit
    for power, digit_char in enumerate(str(num)[::-1]):
        digit = int(digit_char)
        total += digit ** power
    return total
print(sum_dig_for(n))
# print('SUM OF SUMS OF DIGIT')
# l=str(n)
# n = 12345
# ls=[int(d) for d in str(n)]
# s=0
# for i in range(len(ls)):
#     s+=sum(ls[i:])
# print(s)





