# import random

# words = ["pen","carpet","ruler","flower","bottle"]

# # i = random.ramdint(0,len(words)-1)
# # word = words[i]

# word = random.choice (words) # clock
# joon=5

# while joon > 0 :
#     print('-' * len(word))#---

#     user_character = input()#s

#     if  user_character in word:
#         print("yes")

#     else:
#         joon = joon -1
#         print("no")    
import random
word=["pen","carpet","ruler","flower","bottle"]
import random
opportunity=10
computer_guess=random.choice(word)

print("Let's start the game :)")
select=[]
for i in range(len(computer_guess)):
    select.append(computer_guess[i])
    print(" _ ",end=' ')

a = []

for j in range(len(computer_guess)):
    a.append(" - ")

selected=[]
while True:

    guess=input("\n pealse type the guess : ")
    guess=guess.lower()

    if guess not in select :
        opportunity-=1
        selected.append(guess)
        print("\n wrong answer :",opportunity,"your selected word:")
        for n in range(len(selected)):
            print( selected[n], ",", end='')
        print("\n")


    for i in range(len(computer_guess)):

        if guess in select[i]:
            a[i]=str(guess)

    for j in range(len(a)):
        print(a[j],end='')
    if a == select:
        print("\t you win :)")
        break
    if opportunity==0:
        print("You did not win!")
        break