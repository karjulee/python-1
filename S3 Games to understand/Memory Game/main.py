from mg_funs import double_shuffle,display,compare
# step 1: make list or makr images
x = ["red", "blue", "pink", "orange", "yellow"]

# step2: double them and shuffle
y = double_shuffle(x)
guessed =[]
# step3 display the *** data
for i in range(5):
    input("press any key to continue...")
    display(y,guessed)

    # step 4 ask user and print data ** and User data
    u1 = int(input("plz enter first guess: "))
    display(y,guessed,u1)

    # step 5 ask user for second gues and print
    u2 = int(input("plz enter second guess: "))
    display(y,guessed,u1,u2)
    # step 6 compare and keep data visible when matched
    y,guessed = compare(y,guessed,u1,u2)
