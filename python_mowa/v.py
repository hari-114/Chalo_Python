# def min_max(list1):
#     min1=[]
#     max1=[]
#     i=0
#     while i < len(list1):
#         val=list1[i]
#         if val not in min1:
#             if len(min1)<3:
#                 min1.append(val)
#             else:
#                 max_in_min=max(min1)
#                 if val < max_in_min:
#                     min1[min1.index(max_in_min)]=val
#         if val not in max1:
#             if len(max1)<3:
#                 max1.append(val)
#             else:
#                 min_in_max=min(max1)
#                 if val > min_in_max:
#                     max1[max1.index(min_in_max)]=val
#         i+=1
#     min1.sort()
#     max1.sort(reverse=True)
#     return min1,max1
# print(min_max([2,2,3,45,20,30,90,1,2]))
n=6
opt=1
if opt ==1:
    s=0+n
    n=n-1
    while n>0:
        s-=n
        n-=1
        s+=n
        n-=1
print(s)


        




