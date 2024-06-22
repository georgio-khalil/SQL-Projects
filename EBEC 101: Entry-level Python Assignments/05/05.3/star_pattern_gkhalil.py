"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/01/2022

Description:
    This program use a loop with turtle graphic to draw a star pattern that has a user specified number of points.

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    n = int(input("How many points do you want on the star?"))

    a = 360/n
    b=2*a

    setheading((180-b)/-2)
    color('black','green') #black outline and green fill
    begin_fill()
    for i in range (n):
        forward(60)
        left(180-a) #calculating the angle as a function of a
        forward(60)
        right(180-b) #angle as a function of b
    end_fill()





"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
