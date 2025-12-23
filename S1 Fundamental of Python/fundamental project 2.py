# # a number guessing game with 10 changes to find the number between 0 to 100

# # computer random and choose 1 number
# # user choose 1 number
#  # compare 2 num
# # if same = win
#      more than
#     less


import random 
X = random.randint(0,100)


for i in range(10):
    Y = int(input("plz entr nmbr: "))
    if X == Y:
        print("You win")
    elif X > Y:
        print("Too low")
    elif X < Y:
        print("Too high")
    else:
        print("invalid number")

