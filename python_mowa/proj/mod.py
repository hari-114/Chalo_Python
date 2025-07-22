def isPalindrome(string):
    if string == string[::-1]:
        print("Is Palindrome")
    else:
        print("Not Palindrome")

def count_the_vowels(name):
    count=1
    for i in range(len(name)):
        if name[i] == 'a' or name[i] == 'e' or name[i] =='o' or name[i] == 'u' or name[i] == 'i':
            count+=1
        else:
            continue
    return count

def frequency_of_letters(name):
    freq={}
    for char in name:
        if char.isalpha():
            char=char.lower()
            freq[char]=freq.get(char,0)+1
    return freq    

lis=[11228,4253,223,121]
n=len(lis)
st=[]
freq={}
for ele in lis:
    st.append(str(ele))
for i in range(len(st)):
    for dig in st[i]:
        dig=int(dig)
        freq[dig]=freq.get(dig,0)+1
print(freq)
maxim=max(freq.values())
print(maxim)
for k,v in freq.items():
    if v==maxim:
        print(k)




