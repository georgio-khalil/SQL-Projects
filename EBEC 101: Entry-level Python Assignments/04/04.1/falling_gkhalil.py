"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 04.1 - Falling
Date: 09/22/2022

Description:
    This program calculates the distance in meters that an object will travel while falling using a function.

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


"""Write new functions below this line (starting with unit 4)."""

def falling_dist(t):
    return (1/2)*8.87*t**2 #g does not need to be a parameter since it is a constant
    

def main():
    print("Time (s)  Distance (m)")
    print("----------------------")
    for t in range (5,51,5): #51 so that t can take on the value 50
        print(f"{t:8}",end='')
        print(f"{falling_dist(t):14.1f}") #formatting string to match table width
        
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
