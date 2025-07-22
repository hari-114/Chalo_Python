'''#Arithmetic operators
a = 1
b= 30
#swap
a, b = b, a
print(a)
print(b)'''

l1 = [1, 'hari', 500, [1,2,3]]
l1.append(90)
print(l1)
l1.insert(2, 'inserted')
print(l1)
l1.remove(90)
print(l1)
l1.pop(2)
print(l1)

#matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# List comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
# reverse list 
squared_numbers.reverse()
print(squared_numbers)

#without reverse
squared_numbers = [x**2 for x in range(10)][::-1]
print(squared_numbers)
