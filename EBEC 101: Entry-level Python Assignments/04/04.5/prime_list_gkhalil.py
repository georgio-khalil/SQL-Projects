"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 04.5 - Prime List
Date: 09/22/2022

Description:
    This program lists all of the primes from 2 up to a user specified limit.

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
    if a < 2 or a%2 == 0:
        return False
    x=3
    while x*x <= a:
        if a%x == 0:
            return False 
        x = x+2 
    return True 
    
def main():
    n=int(input("Enter a positive integer: "))
    numbers=[] #create an empty list which will contain the prime numbers
    for i in range (2,n+1): #i iterates from 2 to n inclusive looking for prime numbers
        if is_prime(i):
            numbers.append(i) #if number is prime, add it to the list
    print(f"The primes up to {n} are: ",end='')
    print(*numbers,sep=', ') #unpack the list and separate arguments with commas
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
