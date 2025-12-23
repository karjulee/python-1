"""
make a grocessay cmd kind of application in which on starting program
it will give you to buy things or quit
# when you buy things it will add total price
# and when you say end program will give you total bill

"""
#computer ask buy or quit
#if buy, calculate price
#user choose a product
#if not, do nothing
#if user say end program, total  bill
products = {
    'apple': 10,
    'banana': 5,
    'orange': 8,
    'grapes': 15,
    'mango': 12,
    'pineapple': 18,
    'watermelon': 20
}
total = 0
while True and total <30:
    x = input("buy or quit: ")
    if x == "buy":
        user = input(f"please choose the product: from {products}")
        total += products[user]
    elif x=="quit":
        break

print("totla bill is ",total)