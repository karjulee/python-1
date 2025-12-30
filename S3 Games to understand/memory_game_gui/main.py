import turtle
import os
import random
from card import Card
import time

# file_paths = "/Users/tarineesae-lee/Desktop/python-1/S3 Games to understand/memory_game_gui/images"
file_paths = os.path.join("S3 Games to understand", "memory_game_gui", "images") # in macos path is S3 Games to understand/memory_game_gui/images and in windows path is S3 Games to understand\memory_game_gui\images
allfiles_path = os.listdir(file_paths)
back_image_path = os.path.join("S3 Games to understand", "memory_game_gui", "back.gif")
print(allfiles_path)

# double the list of all file names
allfiles_path2x = allfiles_path*2
random.shuffle(allfiles_path2x) # shuffle them


# screen settings
screen = turtle.Screen()
screen.title("Memory Game")
screen.setup(width=1.0, height=1.0)
screen.bgcolor("lightblue")


# register all shapes on screen
for each in allfiles_path2x:
    screen.register_shape(os.path.join(file_paths, each))
screen.register_shape(back_image_path)


xpos = -300
ypos = 280
all_cards = []
screen.tracer(0)
for each in allfiles_path2x:
    full_path = os.path.join(file_paths, each)
    card = Card(full_path, back_image_path)
    card.setup_position(xpos, ypos)
    xpos += 120
    if xpos > 300:
        xpos = -300
        ypos -= 150
    all_cards.append(card)
    
screen.update()
click_number=1

visible_cards = []
selected_card = []


def karju(x, y):
    global click_number
    if click_number==1:
        # when first time clicking the screen
        print("screen clicked at", x, y)
        for card in all_cards:
            if abs(card.back.xcor() - x) < 50 and abs(card.back.ycor() - y) < 70:
                print("card clicked:", card.image_file)
                card.show_front()
                selected_card.append(card)
        click_number=click_number+1
        screen.update()


    elif click_number==2:
        # when second time clicking the screen
        print("screen clicked at", x, y)
        for card in all_cards:
            if abs(card.back.xcor() - x) < 50 and abs(card.back.ycor() - y) < 70:
                print("card clicked:", card.image_file)
                card.show_front()
                selected_card.append(card)
        
        # check if two selected cards are same
        if selected_card[0].image_file == selected_card[1].image_file:
            print("It's a match!")
            visible_cards.append(selected_card[0])
            visible_cards.append(selected_card[1])
        else:
            print("Not a match.")
            # hide the cards again after short delay
            turtle.time.sleep(1)
            for card in selected_card:
                if card not in visible_cards:
                    card.show_back()

        screen.update()
        time.sleep(0.5)
        selected_card.clear()
        click_number=1



screen.onclick(karju)


turtle.done()
