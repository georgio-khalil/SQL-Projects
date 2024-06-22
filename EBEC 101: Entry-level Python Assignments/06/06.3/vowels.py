"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/15/2022

Description:
    This program serves as a module which will be imported via basic import for the Random Vowels assignment.

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


def draw_a():
    """Complete this function to draw the character a."""
    penup()
    forward(60)
    left(90)
    pendown()
    forward(30)
    circle(30,360,20)
    forward(30)
    backward(60)
    right(90)
    penup()


def draw_e():
    """Complete this function to draw the character e."""
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
    """Complete this function to draw the character i."""
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


def draw_o():
    """Complete this function to draw the character o."""
    penup()
    left(90)
    forward(30)
    pendown()
    circle(-30,360,20)
    penup()
    backward(30)
    right(90)
    forward(60)


def draw_u():
    """Complete this function to draw the character u."""
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


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    draw_a()
    forward(20)
    draw_e()
    forward(20)
    draw_i()
    forward(20)
    draw_o()
    forward(20)
    draw_u()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
