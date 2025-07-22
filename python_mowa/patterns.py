rows=10
print('INCREASING')
for row in range(1,rows+1):
    for num in range(1,row+1):
        print(num,end=' ')
    print(' ')

print('Decreasing')

for row in range(1,rows+1):
    for num in range(row,0,-1):
            print(num,end=' ')
    print(' ')

print('Ulta Triangle')

for row in range(rows,0,-1):
    for num in range(1,row+1):
        print(num,end=' ')
    print(' ')


print("              RHOMBUS           ")


for row in range(1,rows+1):
    print(end='  '*int(rows-row))
    for num in range(1,row+1):
        print(num,end=' ')
    for num in range(row-1,0,-1):
        print(num,end=' ')
    print(' ')

for row in range(rows-1,0,-1):
    print(end='  '*int(rows-row))
    for num in range(1,row+1):
        print('*',end=' ')
    
    for num in range(row-1,0,-1):
        print('*',end=' ')
    print(' ')
print()

print("Increasing num Decreasing Alpha")


for row in range(1,rows+1):
    print(end='  '*int(rows-row))
    for num in range(1,row+1):
        print(num,end=' ')
    for num in range(row-1,0,-1):
        print(chr(65+(num-1)),end=' ')
    print(' ')

for row in range(1,rows+1):
    for num in range(1,row+1):
        print(end=' '*int(row-1))
        print('*',end=' ')
    print(' ')