s = 'Hari Vardhan'
lower_count=0
upper_count=0

for char in s:
    if char.islower():
        lower_count+=1
    elif char.isupper():
        upper_count+=1

print(lower_count)
print(upper_count)

s='mom'
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

str1="Shashank"
copy=int(input("Enter Number of copies"))
for i in range(copy):
    print(str1[0:2],end="")
print('\n')


stx='xBannux'
if stx.startswith('x') and stx.endswith('x'):
    stx=stx[1:-1]

print(stx)


copy1=int(input("Enter Number of copies"))
for i in range(copy1):
    print(str1[-3:],end="")






