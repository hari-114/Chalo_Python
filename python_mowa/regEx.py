import re
pattern='abcma'
string='aabcmadbyabc'
#re.compile(pattern)
print(re.match(pattern,string)) #pattern matching at begining
print(re.search(pattern,string)) #pattern matching anywhere
print(re.search(pattern,string).group()) #returns matched pattern
print(re.search(pattern,string).start()) #returns starting position of pattern
print(re.search(pattern,string).end()) #last position
print(re.search(pattern,string).span()) #start and last

text = '''This is a -- Sample
And a  Second line'''
pattern= '(^\w+)|(\w+\S*$)'  #alpha-numeric and non white spaces
single_line=re.compile(pattern)
multiline=re.compile(pattern,re.MULTILINE)
print(single_line.findall(text))
print(multiline.findall(text))

s='123-908-784'
m=re.search('(\d+)-(\d+)-(\d+)',s)
print(m.groups()[0])

s1='Hello'
pat='^H...o$'
mat=re.search(pat,s1)
print(mat)

#1
str=['789','123','004']

for s in str:
    if re.fullmatch(r'[0-7]+',s):
        print(f"'{s}' is octal")
    else:
        print(f"'{s}' is not octal")

#2
emails="""donthula89@facebook.com
hari67@google.com
Bannu09@micro.in"""
print(f'Emails:\n{emails}')
Upat='(^\w+)'
user=re.compile(Upat,re.MULTILINE)
print("User IDs")
print(user.findall(emails))
dmail=re.compile('@(\w+)',re.MULTILINE)
suffix=re.compile('(\w+$)',re.MULTILINE)
print("Domains")
print(dmail.findall(emails))
print('Suffix')
print(suffix.findall(emails))

#3
line="""A, very  very; irregular_sentence"""
pat=r'[a-zA-Z0-9]+'
oc=re.compile(pat,re.MULTILINE)
li=oc.findall(line)
print((' '.join(li)))

#4
tweet='''Good advice! RT @TheNextWeb: What I would do Differently if I was learning to code today
http://t.co/ghfcwugf cc: @garyberhardt #rstarts'''
tweet = re.sub(r'http\S+','',tweet)
tweet=re.sub(r'RT|cc','',tweet)
tweet=re.sub(r'[@#]\w+','',tweet)
tweet=re.sub(r'[^\w\s]','',tweet)
tweet=re.sub(r'\s+',' ',tweet)
tweet=tweet.strip()
print(tweet)


def similar(str1, str2):
    pattern=str1.replace('_','.')
    pattern=f"^{pattern}$"
    words=str2.split(':')
    matches=[word.upper() for word in words if re.match(pattern,word,re.IGNORECASE)]
    return ':'.join(matches)

str1="Fi_er"
str2="Fever:filer:Filter:Fixer:fiber:fibre:tailor:offer"
print(similar(str1,str2))






