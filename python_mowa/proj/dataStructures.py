print('P1')
d1={'Hari':'Bhakti','Shashank':'chill guy','Vikarthan':'Funny','Adithya':'Diplomatic'}
print(d1)
d1['Ram']='Dharmic'
print(d1)
d1['Hari']='Sanathani'
print(d1)

print('P2')
scores=[20,90,89,79,99]
scores.sort()
print(scores[-2])

print('P3')
marks_list={'Shashank':[80,89,70],
            'Vikartan':[70,90,80],
            'Hari':[70,90,78]}

name=str(input("Enter a name: "))
if name in marks_list:
    marks=marks_list[name]
    avg=sum(marks)/len(marks)
    print(f'Average percentage marks: {avg%.2}')

print('P4')

string="Ram is good Ram is Rightegeous Ram Bye"
split=string.split()
naam="Ram"
count=0
print(split)
for i in range(len(split)):
    if split[i] == naam:
        count+=1
print(count)

import mod as ds

ds.isPalindrome('bob')
print(ds.count_the_vowels('Hari'))
print(ds.frequency_of_letters('Hari vardhan'))


