import turtle


class Card:
    def __init__(self, image_file):
        self.front = turtle.Turtle()
        self.back = turtle.Turtle()

    def register_images(self, screen, image_file):
        screen.register_shape(image_file)
        self.front.shape(image_file)
        self.front.hideturtle()
        self.back.shape("square")
        self.back.shapesize(stretch_wid=7, stretch_len=5)
        self.back.color("gray")

    def setup_position(self, x, y):
        self.front.penup()
        self.back.penup()
        self.front.goto(x, y)
        self.back.goto(x, y)
        self.back.showturtle()

    def show_front(self):
        self.back.hideturtle()
        self.front.showturtle()
    def hide_front(self):
        self.front.hideturtle()
        self.back.showturtle()


        
