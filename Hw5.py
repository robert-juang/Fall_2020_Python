# #1.
big_total = 0
maximum_share = 0

def div_w_remainder(dividend,divisor):
    whole = dividend//divisor
    remainder = dividend%divisor
    return(whole,remainder)

def share_items(number_of_things,number_of_people):
    global big_total
    global maximum_share
    whole, remainder = div_w_remainder(number_of_things,number_of_people)
    big_total = big_total + number_of_things
    maximum_share = maximum_share + whole
    if remainder > 1:
        maximum_share += 1
    return(big_total, maximum_share)

def question_1():
    print(share_items(10,4))
    print(share_items(20,3))
    print(share_items(14,7))

question_1()

#2 and 3.
import turtle
import random

my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_screen.colormode(255)
screen_size_multiplier = 0.5

screen_width,screen_height=my_screen.screensize()

def big_rectangle():
    my_turtle.pu()
    my_turtle.setposition(screen_size_multiplier*screen_width,0)
    my_turtle.pd()
    my_turtle.setposition(screen_size_multiplier*screen_width,screen_size_multiplier*screen_height)
    my_turtle.setposition(-1*screen_size_multiplier*screen_width,screen_size_multiplier*screen_height)
    my_turtle.setposition(-1*screen_size_multiplier*screen_width,-1*screen_size_multiplier*screen_height)
    my_turtle.setposition(screen_size_multiplier*screen_width,-1*screen_size_multiplier*screen_height)
    my_turtle.setposition(screen_size_multiplier*screen_width,0)


def head(scale):

    my_turtle.pd()
    my_turtle.circle(scale*5,extent=360)

def body(scale):
    my_turtle.right(90)
    my_turtle.fd(scale*5)
    my_turtle.pd()
    my_turtle.right(180)
    my_turtle.fd(scale*3)

def two_arms(scale):
    my_turtle.pu
    my_turtle.right(60)
    my_turtle.fd(scale*5)
    my_turtle.pd
    my_turtle.left(180)
    my_turtle.fd(scale*5)
    my_turtle.pu
    my_turtle.right(60)
    my_turtle.fd(scale*5)
    my_turtle.pd
    my_turtle.left(180)
    my_turtle.fd(scale*5)
    my_turtle.right(60)

def two_legs(scale):
    my_turtle.fd(scale*5)
    my_turtle.right(40)
    my_turtle.pu
    my_turtle.fd(scale*5)
    my_turtle.left(180)
    my_turtle.fd(scale*5)
    my_turtle.right(90)
    my_turtle.fd(scale*5)
    my_turtle.right(180)
    my_turtle.fd(scale*5)
    my_turtle.pd

def face(scale):
    my_turtle.pu()
    my_turtle.right(50)
    my_turtle.fd(scale*13)
    my_turtle.right(90)
    my_turtle.fd(scale*2)
    my_turtle.pd()
    my_turtle.circle(scale/2,extent=360)
    my_turtle.left(170)
    my_turtle.pu()
    my_turtle.fd(scale*4)
    my_turtle.pd()
    my_turtle.circle(scale/2,extent=360)
    my_turtle.left(100)
    my_turtle.pu()
    my_turtle.fd(scale*4)
    my_turtle.pd()
    my_turtle.circle(scale*2,extent=180)

def makedude(scale):
    head(scale)
    body(scale)
    two_arms(scale)
    two_legs(scale)
    face(scale)
def random_stickfigure():
    scale = random.randint(0,10)
    my_turtle.pu()
    x_position = random.randint(int(-1*screen_size_multiplier*screen_width),int(screen_size_multiplier*screen_width))
    y_position = random.randint(int(-1*screen_size_multiplier*screen_height),int(screen_size_multiplier*screen_height))
    my_turtle.setposition(x_position,y_position)
    makedude(scale)

def many_random_stickfigure():
    my_turtle.speed(10)
    for i in range(random.randint(1,50)):
        random_stickfigure()

many_random_stickfigure()
