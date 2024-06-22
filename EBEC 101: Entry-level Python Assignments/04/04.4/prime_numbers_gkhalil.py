"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 09/22/2022

Description:
    This program displays whether a given number is prime or not. User should enter -1 to quit the program.

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

def is_prime(a):
    if a == 2:
        return True
    if a < 2 or a%2 == 0: #checks if number is even or 0 or 1
        return False
    x=3
    while x*x <= a: #we don't have to check all possible divisors, we only need to check divisors less than sqrt(a). If a is not divisible by any number less than sqrt(a), it means that a is prime.
        if a%x == 0:
            return False 
        x = x+2 #only odd numbers because we know that a is not divisible by 2 at this point
    return True #for example, for a=11, it is enough to check if it is divisible by 3 only because square root of 11 is less than 4
    
def main():
    while 1:
        a=int(input("Enter a positive integer (-1 to quit): "))
        if a==-1:
            return #quit the program if entered number is -1
        if is_prime(a):
            print(f"  {a} is prime!")
            continue
        print(f"  {a} is not prime.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
