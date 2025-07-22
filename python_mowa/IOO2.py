# f1=open('sample.txt','r')
# read=f1.read()
# l=read.split()
# print(l)
# longest=0
# word=''
# for i in l:
#     if len(i)>longest:
#         longest=len(i)
#         word=i
# print(word)
# f1.close()

# def frequency_of_letters(name):
#     freq={}
#     for char in name:
#         if char.isalpha():
#             char=char.lower()
#             freq[char]=freq.get(char,0)+1
#     return freq   

# print(frequency_of_letters(read)) 

def secret_code(file):
    def num_of_lines(file):
        num_lines=0
        time='AM'
        with open(file,'r') as f:
            for line in f:
                num_lines+=1
        if num_lines>=12 and num_lines<=24:
            num_lines-=12
            time='PM'
            print(f'Meeting time: {num_lines}{time}')
        elif num_lines<12 and num_lines>0:
            print(f'Meeting time: {num_lines}{time}')
        else:
            print('No time')

    def rep_of_words(file):
        with open(file,'r') as f:
            read=f.read()
            lst=read.split()
            count={}
            c=[]
            for word in lst:
                word = word.strip('.,!?;:()[]{}"\'')
                count[word]=count.get(word,0)+1
            max_word=max(count,key=count.get)
            print(f'Meeting PLace: {max_word} Street')
    num_of_lines(file)
    rep_of_words(file)

secret_code('sample.txt')