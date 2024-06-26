"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 08.4 - Number Writer
Date: 11/06/2022

Description:
    This program writes a user defined number of random integers to a file named random_numbers.txt.

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
import random as r

"""Write new functions below this line (starting with unit 4)."""

def main():
    n=int(input("How many numbers would you like? ")) #n is the desired number of integers

    with open('random_numbers.txt','w') as fo:
        for i in range(n):
            fo.write(''.join([str(r.randint(1019,1215)),'\n'])) #generate a random number between 1019 and 1215 inclusive and join it with an endline character

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
