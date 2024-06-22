"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 10/02/2022

Description:
    This program displays the message "Mississippi Turtles" using letters drawn by the turtle.

Contributors:

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")


def draw_e():
    """Write this function."""
    penup()
    left(90)
    forward(30)
    right(90)
    pendown()
    forward(60)
    left(90)
    circle(30,315,15)
    penup()
    circle(30,45,2)
    setheading(-90)
    forward(30)
    left(90)
    

def draw_i():
    """Write this function."""
    penup()
    left(90)
    pendown()
    forward(60)
    penup()
    forward(20)
    pendown()
    dot(10)
    penup()
    backward(80)
    right(90)


def draw_l():
    """Write this function."""
    penup()
    left(90)
    pendown()
    forward(120)
    penup()
    backward(120)
    right(90)

def draw_M():
    """Write this function."""
    pendown()
    left(90)
    forward(80)
    circle(-15,180,6)
    forward(80)
    penup()
    backward(80)
    right(180)
    pendown()
    circle(-15,180,6)
    forward(80)
    left(90)
    penup()

def draw_p():
    """Write this function."""
    pendown()
    left(90)
    forward(60)
    backward(120)
    forward(90)
    circle(-30,360,18)
    penup()
    backward(30)
    right(90)
    forward(60)



def draw_r():
    """Write this function."""
    pendown()
    left(90)
    forward(60)
    backward(60)
    forward(30)
    circle(-30,90,10)
    penup()
    right(90)
    forward(60)
    left(90)
    


def draw_s():
    """Write this function."""
    pendown()
    forward(15)
    circle(15,180,10)
    circle(-15,180,10)
    forward(15)
    penup()
    right(90)
    forward(60)
    left(90)

def draw_t():
    """Write this function."""
    penup()
    forward(30)
    left(90)
    pendown()
    forward(120)
    backward(30)
    left(90)
    forward(30)
    backward(60)
    left(90)
    penup()
    forward(90)
    left(90)

def draw_u():
    """Write this function."""
    penup()
    left(90)
    forward(60)
    pendown()
    backward(30)
    right(180)
    circle(30,180,9)
    forward(30)
    backward(60)
    right(90)
    penup()

def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    speed(50) #configurable speed
    penup()
    goto(-250,80) #northwest part of canvas
    draw_M()
    forward(20) #space between every letter
    draw_i()
    forward(20)
    draw_s()
    forward(20)
    draw_s()
    forward(20)
    draw_i()
    forward(20)
    draw_s()
    forward(20)
    draw_s()
    forward(20)
    draw_i()
    forward(20)
    draw_p()
    forward(20)
    draw_p()
    forward(20)
    draw_i()
    penup()
    goto(-250,-120)
    draw_t()
    forward(20)
    draw_u()
    forward(20)
    draw_r()
    forward(20)
    draw_t()
    forward(20)
    draw_l()
    forward(20)
    draw_e()
    forward(20)
    draw_s()
    forward(20)

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
