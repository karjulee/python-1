# list of 5 words
x = ["apple","orange","banana","coconut","watermelon"]
print(x)
# duplications
x = x*2
print(x)

# shuffle randomly
import random
random.shuffle(x)


match =0
guess = 0
# in loop ask user to enter first positon
#   ask your to enter second position
#   if matching make match +=1 and guess+=1; 
#       and remove them from list and show updated list
#   if not mathicng make guess+=1
while len(x)!=0:
    for i in range(len(x)):
        print(f"*{i}*",end=" ")
    print()
    ind1 = int(input("please enter your first positions"))
    if ind1>len(x) or ind1<0:
        print("hey!!! wrong please write proper size")
        continue
    card1 = x[ind1]
    print(f"you have selected: 1st **{card1}**")
    ind2 = int(input("please enter your first positions"))
    card2 = x[ind2]
    print(f"you have selected: wnd **{card2}**")
    if card1 == card2:
        print("matching")
        x.remove(card1)
        x.remove(card2)
        match+=1
        guess+=1

    else:
        print("not matching")
        guess+=1

    print(f"Guesses = {guess}, Matching = {match}")