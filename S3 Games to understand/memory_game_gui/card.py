import turtle


class Card:
    def __init__(self, image_file, back_image_file):
        self.front = turtle.Turtle(shape=image_file) # shape is gif image
        self.back = turtle.Turtle(shape=back_image_file) # shape is gif image
        self.image_file = image_file
        self.front.penup()
        self.back.penup()

    def setup_position(self, x, y):
        self.front.goto(x, y)
        self.back.goto(x, y)

    def show_front(self):
        self.back.hideturtle()
        print("back is hidden")
        self.front.showturtle()

    def show_back(self):
        self.front.hideturtle()
        print("front is hidden")
        self.back.showturtle()

        

if __name__ == "__main__": # if i import this file this part will not run
    # register shape

    turtle.Screen().register_shape(r"S3 Games to understand/memory_game_gui/images/" \
    "dog2.gif")
    turtle.Screen().register_shape(r"S3 Games to understand/memory_game_gui/back.gif")

    card = Card(r"S3 Games to understand/memory_game_gui/images/dog2.gif", r"S3 Games to understand/memory_game_gui/back.gif")

    card.setup_position(100, 0)
    input("Press Enter to show front")
    card.show_front()
    input("Press Enter to show back")
    card.show_back()
    turtle.done()