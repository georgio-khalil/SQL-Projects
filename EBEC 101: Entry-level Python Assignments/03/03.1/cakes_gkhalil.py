"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/08/2022

Description:
    This program uses nested loops to draw a cake with a given number of layers.

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
    l = int(input("Enter the number of layers: "))

    for i in range(l):
        for j in range(l-i-1):
            print(' ',end='') #print l-i-1 spaces (if l is 6, 5 spaces at first outer loop iteration, then 4,3,2,1,0)
        print('[',end='')
        for k in range(2*i+1): #print odd number of stars, increasing with every outer loop iteration
            print('*',end='')
        print(']')
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
