"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/31/2022

Description:
    This program returns whether a given matrix of numbers represents a Lo Shu magic square or not

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


def print_square(l): #to print the magic square
    for i in range(3):
        print(" ",end='')
        for j in range(3):
            print(f" {l[i][j]}",end='')
        print("")

def num_req(l): #to check number requirement
    vect=[] #linear representation of list
    for i in range(3):
        for j in range(3):
            vect.append(l[i][j])

    for i in range(1,10):
        if vect.count(i) != 1:
            return False
    return True

def rows_req(l): #to check row requirement
    for r in range(3):
        row_sum=0
        for c in range(3):
            row_sum=row_sum+l[r][c] #fixing row and iterating through columns
        if row_sum != 15:
            return False
    return True

def cols_req(l): #to check column requirement
    for c in range(3):
        col_sum=0
        for r in range(3):
            col_sum=col_sum+l[r][c] #fixing column and iterating through rows
        if col_sum != 15:
            return False
    return True

def diag_req(l): #to check diagonal requirement
    diag_sum1=l[0][0]+l[1][1]+l[2][2]
    diag_sum2=l[2][0]+l[1][1]+l[0][2]
    if diag_sum1 == 15 and diag_sum2 == 15:
        return True
    return False

def is_magic(l): #to check if magic or not
    if num_req(l) and rows_req(l) and cols_req(l) and diag_req(l):
        return True
    return False

def print_magic(l): #to print correct message
    if is_magic(l):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")

def main():
    l_1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    l_2=[[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    l_3=[[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    
    print("Your square is:")
    print_square(l_1)
    print_magic(l_1)
    print("")
    print("Your square is:")
    print_square(l_2)
    print_magic(l_2)
    print("")
    print("Your square is:")
    print_square(l_3)
    print_magic(l_3)
    print("")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
