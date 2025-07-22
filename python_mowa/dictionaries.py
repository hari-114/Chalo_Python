dic1={0:10, 1:20}
print(dic1)

#appending
dic1[2]=30
print(dic1)

#merging 3 dictionaries
print("MERGING DICTIONARIES")
dic2={3:40,4:50}
dic3={5:60,6:70}
dic= dic1|dic2|dic3
print(dic)

print("CHECKING IF KEY EXISTS OR NOT")
key = int(input('Enter a key to search'))
if(key in dic):
    print('key exists')
else:
    print('not exists') 

print("PRINTING VALUES AND KEYS")
DIC1={'A':10,'B':20,'C':50}
for i in DIC1:
    print(i,DIC1[i])

print("STORING KEYS WITH VALUES OF ITS SQUARES ")
sqtdic={}
for i in range(1,16):
    sqtdic[i]=i**2
print(sqtdic)

print("PRINING SUM OF ALL VALUES")
sum=0
for i in dic.values():
    if isinstance(i, int):
        sum+=i

print('sum of values in dictionary '+ str(sum))
