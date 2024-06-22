"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/14/2022

Description:
    This program prompts the user to calculate the sum of two random integers. The program then tells the user whether the answer is correct or not.

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

def random_number(d):
    return r.randrange(10**(d-1),10**(d)) #10^(d-1) is the lowest d digit number and 10^(d) is the lowest d+1 digit number which we are not including
def main():
    two_d=random_number(2) #need to store the random numbers to check if the answer is correct
    three_d=random_number(3)
    print(f"{two_d:5}") #width 5 for alignment
    print(f"+ {three_d}")
    print("-----")
    a=int(input("= "))
    if a == two_d+three_d:
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {two_d+three_d}.")
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
