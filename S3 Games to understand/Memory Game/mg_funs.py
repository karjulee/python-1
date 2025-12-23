import random

def double_shuffle(data:list):
    data = data*2
    random.shuffle(data)
    return data

def display(data:list ,guessed, u1=None, u2 = None):
    for i in range(len(data)):
        if u1==i or u2==i or i in guessed:
            print(f"[{i}]-->{data[i]}")
        else:
            print(f"[{i}]-->****")

def compare(data:list,guessed, u1=None, u2 = None):
    val1 = data[u1]
    val2 = data[u2]
    if val1 == val2:
        print('match')
        guessed.append(u1)
        guessed.append(u2)
    else:
        print("not match")
    return data, guessed