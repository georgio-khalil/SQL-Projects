"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/15/2022

Description:
    This program displays the sum and average of a given series of numbers

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
    n = 0
    sum = 0
    avg = 0
    count = int(0)

    while 1: #perpetual while loop
        n = float(input("Enter a non-negative number (negative to quit): "))
        if n <0:
            break #when input is negative, break from loop
        sum = sum + n #compute sum as input is given
        count = count + 1 #track number of inputs

    if count ==0:
        print("  You didn't enter any numbers.")
    else:
        avg = sum/count
        print(f"  You entered {count} numbers.")
        print(f"  Their sum is {sum:.3f} and their average is {avg:.3f}.")
    



        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
