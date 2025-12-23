import turtle


class Card:
    def __init__(self, image_file, back_image_file):
        self.front = turtle.Turtle()
        self.back = turtle.Turtle()
        self.image_file = image_file
        self.back_image_file = back_image_file

    def register_images(self, screen, image_file):
        screen.register_shape(image_file)
        self.front.shape(image_file)
        screen.register_shape(self.back_image_file)
        self.back.shape(self.back_image_file)


    def setup_position(self, x, y):
        self.front.penup()
        self.back.penup()
        self.front.goto(x, y)
        self.back.goto(x, y)
        self.back.showturtle()

    def show_front(self):
        self.back.hideturtle()
        self.back.hideturtle()
        print("back is hidden")
        self.front.showturtle()
    def show_back(self):
        self.front.hideturtle()
        self.back.showturtle()

        
