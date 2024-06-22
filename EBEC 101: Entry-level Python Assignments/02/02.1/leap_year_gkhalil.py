"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/08/2022

Description:
    This program returns whether the given year is a leap year and the number of days of the month of February in that year.

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

    year = float(input("Enter a year: "))

    #determine whether year is divisible by 100
    if year%100 == 0: #if year is divisible by 100
        if year%400 == 0: #if year is divisible by 100 and 400
            print (f"The year {year:.0f} is a leap year.\nFebruary of {year:.0f} has 29 days.")
        else: #if year is divisible by 100 but not 400
            print (f"The year {year:.0f} is not a leap year.\nFebruary of {year:.0f} has 28 days.")
    else: #if year is not divisible by 100
        if year%4 == 0: #if year is not divisible by 100 but is divisible by 4
            print (f"The year {year:.0f} is a leap year.\nFebruary of {year:.0f} has 29 days.")
        else: #if year is not divisible by 100 nor 4
            print (f"The year {year:.0f} is not a leap year.\nFebruary of {year:.0f} has 28 days.")
            
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
