# load the text file and increase price and save back
file = open("fruits.txt",'r')
# now read file
data = file.read()
# now store data as or dictionary
# there is split function that can change data from string to list
data_list = data.split("\n")
output = '' # 
for each in data_list:
    f,p = each.split(" ")
    print(f'the fruit name is {f} and its price os {p}')
    new_price = float(p) * 1.1 # 10 percent
    print(f'New price is {new_price}')
    output = output + f"{f},{round(new_price,2)}\n"


file2 = open("fruits2.txt",'w')# w means weire
file2.write(output)