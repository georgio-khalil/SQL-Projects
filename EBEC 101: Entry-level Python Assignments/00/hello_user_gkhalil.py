"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 00.1 - Hello User
Date: 08/25/2022

Description:
    This program prompts the user to enter their name then returns a greeting followed by the inputted name.

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


def main():
    name = input("What is your name? ") #computer sends prompt, inputted name is saved in variable "name"
    print(f"Hello {name}!") #computer prints "Hello" followed by inputted name and exclamation mark

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
