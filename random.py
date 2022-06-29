import random

array=[]

le = int(input("Please type the number of array members : "))

while le != len(array) :
    s = random.randint(0 , 20)

    if s not in array:
   
       
       array.append(s)
      
print("ara:" , array )