"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/08/2022

Description:
    This program returns the applied quantity discount (if any) on software package sales for the specified quantity. 

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

    packages = float(input("How many packages will be purchased: "))

    if packages < 0: #if package amount is negative
        print ("  Invalid Input!")
    elif packages >=0: #if package amount is positive
        if packages <4: #quantities 0 to 3
            price = packages*880
            print ("  No discount applied.")
            print (f"  The total price to purchase {packages:.0f} packages is ${price:,.2f}.")
        elif packages <40: #quantities 4 to 39
            discount = 0.1
            price = packages*880*(1-discount)
            print (f"  {discount:0.0%} discount applied.")
            print (f"  The total price to purchase {packages:.0f} packages is ${price:,.2f}.")
        elif packages <200: #quantities 40 to 199
            discount = 0.15
            price = packages*880*(1-discount)
            print (f"  {discount:0.0%} discount applied.")
            print (f"  The total price to purchase {packages:.0f} packages is ${price:,.2f}.")
        elif packages <1000: #quantities 200 to 999
            discount = 0.3
            price = packages*880*(1-discount)
            print (f"  {discount:0.0%} discount applied.")
            print (f"  The total price to purchase {packages:.0f} packages is ${price:,.2f}.")
        else: #quantities 1000 or more
            discount = 0.42
            price = packages*880*(1-discount)
            print (f"  {discount:0.0%} discount applied.")
            print (f"  The total price to purchase {packages:.0f} packages is ${price:,.2f}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
