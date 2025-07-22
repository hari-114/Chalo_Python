#map
def cube(num):
    return num**3
list1=[1,2,3,4,5,6,7,8,9]
cubes=map(cube,list1)
print(list(cubes))
li=[x**3 for x in range(1,10) if x%2==0]
print(li)


#reduce
from functools import reduce
def mul(x,y):
    return x*y
sum = reduce(mul,list1)
print(sum)


#filter
def even(num):
    if num%2==0:
        return num
even1=filter(even,list1)
print(even1)
print(list(even1))


#lamda
squares=list(map(lambda x: x**2,list1))
print(squares)

