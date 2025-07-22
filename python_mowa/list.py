list = [1,2,3,4,5]
for i in range(len(list)):
    print(list[i])

#appending
list.append('Hari')
print(list)
#reversing
print(list[::-1])

#listing
'''list1=[]
for i in range(5):
    list1.append(input())
cnt = (input("enter number to know count"))
print(list1)
print(list1.count(cnt))'''

#merging 2 lists
l1=[1,2,3,4]
l2=[7,8,55,9]
print('list 1')
print(l1)
print('list2')
print(l2)
l3=l1+l2
print('Merged List') 
print(l3)

#appending after index
print('After Apending usind index')
l2.insert(2,10)
print(l2)

#removing element at specific index
l2.remove(7)
print(l2)

#remove repeated elements
def occur(list, n):
    count = 0
    for i in range(len(list)):
        if list[i]==n :
            count +=1
            if count == 2:
                del list[i]
                break
    return list

l5=[1,2,2,1,2,3]
print(occur(l5,1))

