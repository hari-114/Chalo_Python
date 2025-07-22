n = 234214
def sep_num(n):
    l=[]
    while n>0:
        digit=n%10
        l.append(digit)
        n=n//10
    print(l[::-1])

def count_num(n):
    l=[]
    while n>0:
        digit=n%10
        l.append(digit)
        n=n//10
    print("count of digits: " + str(len(l)))

def to_integer(n):
    result=0
    power=0
    while n>0:
        digit=n%10
        result+=digit*(2**power)
        power+=1
        n//=10
    return result


def to_binary(n):
    binary=''
    while n>0:
        remainder=n%2
        binary=str(remainder)+binary
        n=n//2
    return binary
    
arr=[]
for i in range(10):
    arr.append(int(input('>')))
print(arr)
print(sum(arr))
avg=sum(arr)//len(arr)
print(f'Average: {avg}')
count=0
for i in range(len(arr)):
    if avg>arr[i]:
        count+=1
    else:
        continue

print(count)

sum=0
for i in range(len(arr)):
    sum+=arr[i]

print(sum)