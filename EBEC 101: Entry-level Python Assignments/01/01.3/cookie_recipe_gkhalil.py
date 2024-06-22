"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/08/2022

Description:
    This program calculates the number of cups of butter, sugar, and flour needed to make a specified number of cookies.

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
    cookies = float(input("How many cookies do you want to make? "))
    #this is to gather inputs. float is added to preserve decimal part of number and use in future calculations
    
    butter = (1.25/48)*cookies
    sugar =  (1.5/48)*cookies
    flour = (2.5/48)*cookies
    #calculate ingredient amounts according to the specified recipe (rule of three)

    #display results. output width is set to 10 and decimal precision to 2
    print(f"To make {cookies:,.0f} cookies, you will need:")
    print(f"{butter:10,.2f} cups of butter")
    print(f"{sugar:10,.2f} cups of sugar")
    print(f"{flour:10,.2f} cups of flour")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
