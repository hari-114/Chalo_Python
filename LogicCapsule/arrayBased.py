
def decresing_seq(list):
    output1=0
    output2=0
    i=0
    while i < len(list)-1:
        if list[i]>list[i+1]:
            length=2
            j= i+ 1
            while j < len(list)-1 and list[j]>list[j+1]:
                length+=1
                j+=1
            output1+=1
            output2=max(length,output2)
            i=j+1
        else:
            i+=1
    return output1,output2


def enc(lst):
    n= len(lst)
    original=[0]*n
    original[n-1]=lst[n-1]
    for i in range(n-2,-1,-1):
        original[i]=lst[i]-original[i+1]
    add=sum(original)
    print(original)
    print(original[0])
    print(add)


    