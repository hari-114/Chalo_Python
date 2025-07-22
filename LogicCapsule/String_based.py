#FindStringCode
def letter_position(ch):
    return ord(ch.upper())-ord('A')+1
def pwords(word):
    total=0
    n=len(word)
    for i in range((n+1)//2):
        if i == n-i-1:
            total+=letter_position(word[i])
        else:
            total+=abs(letter_position(word[i])-letter_position(word[n-i-1]))
    return total
def Fsc(sentence):
    words=sentence.split()
    result=''.join(str(pwords(word)) for word in words)
    return int(result)


#Addition using strings
def add_strings(str1,str2):
    num1,num2=int(str1),int(str2)
    if num1>=0 and num2>=0:
        sum=num1+num2
    return str(sum)


#Get code through Strings
def string_code(str):
    lst=str.split()
    word_lst=[]
    for word in lst:
        word_lst.append(len(word))
    word_sum=sum(word_lst)
    while word_sum>=10:
        temp=0
        while word_sum > 0:
            digit=word_sum%10
            temp+=digit
            word_sum//=10
        word_sum=temp
    return word_sum

#input1: Fi_er
#input2: fiber:Fiver:faber:Fixer:olymp
#output: FIBER:FIVER:FIXER
w1='Fi_er'
w1.lower()
words='fiber:Fiver:faber:Fixer:olymp'

w_lis=words.lower().split(":")
if '_' in w1:
    under=w1.index('_')
print(under)
print(w_lis)
# for word in w_lis:
#     if len(word)==len(w1):
