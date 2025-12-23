import turtle
import os
import random
from card import Card

file_paths = "/Users/tarineesae-lee/Desktop/python-1/S3 Games to understand/memory_game_gui/images"
allfiles_path = os.listdir(file_paths)

allfiles_path2x = allfiles_path*2
random.shuffle(allfiles_path2x)

# screen settings
screen = turtle.Screen()
screen.title("Memory Game")
screen.setup(width=1.0, height=1.0)
screen.bgcolor("lightblue")

screen.tracer(0)
xpos = -300
ypos = 280
all_cards = []
for each in allfiles_path2x:
    card = Card(each)
    card.register_images(screen, os.path.join(file_paths, each))
    card.setup_position(xpos, ypos)
    xpos += 120
    if xpos > 300:
        xpos = -300
        ypos -= 150
    all_cards.append(card)

def karju(x, y):
    print("screen clicked at", x, y)
    for card in all_cards:
        if abs(card.back.xcor() - x) < 50 and abs(card.back.ycor() - y) < 70:
            card.show_front()
    


screen.onclick(karju)

screen.update()

turtle.done()
