# f1=open('sample.txt','r')
# print(f1.read())
# f1.close()
# print('------------------------------------------------------------')
# f2=open('sample.txt')
# line1=f2.readline()
# line2=f2.readline()
# print(line1)
# print(line2)
# print(f2.readline())
# f2.close()
# print('------------------------------------------------------------')
f3=open('sample.txt')
listOfLines=f3.readlines()
print(listOfLines)
f3.close()

# f1=open('sample.txt','w') #write mode
# f1=open('sample.txt','a')  #append mode
# msg = input("Enter to append: ")
# f1.write(msg)
# f1.close()

# f1=open('Udharan.txt','x') #create mode
# f1.write("Ahimsa Pradamo Dharma \n Dharma Himsa Tadaivacha")
# f1.close()

# import os
# result = os.path.exists('C:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\Shiva')
# if result==True:
#     print('Folder exsists')
# else:
#     os.mkdir('C:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\Shiva')
#     print('FolderCreated')

# import os
# result = os.path.exists('C:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\Shiva')
# if result==True:
#     os.rmdir('C:\\Users\\hariv\\OneDrive\\Dokumen\\na Stuffuu\\Chalo Python\\python_mowa\\Shiva')
#     print('file deleted')
# else:
#     print('not exist')

