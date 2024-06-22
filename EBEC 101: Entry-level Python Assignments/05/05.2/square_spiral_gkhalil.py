"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 05.2 - Square Spiral
Date: 10/01/2022

Description:
    This program instructs a turtle to draw a square spiral.

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
    setup(564, 564)
    width(5)


def main():
    setheading(45)
    for i in range (29):
        forward(12+12*i) #first iteration is 12 pixels, then increase by 12 every iteration
        right(90) #turn 90 after every forward step


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
