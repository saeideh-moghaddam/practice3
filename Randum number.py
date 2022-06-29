import random
a=[]
cou= int (input("Please type the count array :"))
for i in range (cou):
    ozv = int(input("Please type the namber :"))
    a.append(ozv)
flag= True

for  i in range (len(a) -1 ) :
    if a[i] > a [i+1] :
        flag=False
        break
if flag:
    print ('sort')    
else :
    print("no sort")
print(a)    
