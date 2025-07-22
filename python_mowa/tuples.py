tup = (1,3,4,5,22)
print(tup)
print(tup[3],tup[-4]) #tuple 4th element from last and 4th element from 1st

n=22
if n in tup:
    print("Exists")
else:
    print("Not exists")

t2l=list(tup)
print(t2l)

for i in range(len(tup)):
    if n == tup[i]:
        print(i)

l1=[(10,20,40),(40,50,60),(70,80,90)]

updated=[]
for t in l1:
    updated.append(t[:-1]+(100,))
print(updated)
updated=[t[:-1]+(100,)for t in l1]
print(updated)


    
    
    