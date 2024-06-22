"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 01.2 - Interest
Date: 09/08/2022

Description:
    This program calculates the future balance of an interest-earning savings account after asking for the initial deposit, annual interest rate, number of years, and times interest is compounded.

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
    print("Enter the following parameters.")
    
    P = float(input("  The initial deposit? "))
    r = float(input("  The annual interest rate in percent? "))
    t = float(input("  The number of years the account earn interest? "))
    n = float(input("  The number of times interest is compounded each year: "))
    #this is to gather inputs. float is added to preserve decimal part of number and use in future calculations

    FV = P*pow(1+(0.01*r)/n,n*t) #calculate future account balance. r is given in percent so a conversion is necessary
    print(f"The balance of this account will be ${FV:10,.2f} after {t:.1f} years.") #display future account balance

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
