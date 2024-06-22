"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/17/2022

Description:
    This program calculates the average rainfall over a period of years using given data.

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
    y = int(input("Enter the number of years: "))
    if y<1:
        print("Invalid input; years must be greater than 0.")
    else:
        total=0
        avg=0
        all_months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for i in range(y): #outer loop runs for every year
            print(f"  For year No. {i+1}")
            for j in range(12): #inner loop runs for every month
                month=all_months[j] #picking month from array according to loop iteration
                while 1:
                    rain_m=float(input(f"    Enter the rainfall for {month}.: "))
                    if rain_m>=0:
                        break
                    print("    Invalid input; rainfall cannot be negative.")
                total=total+rain_m
        number_months=12*y
        avg=total/number_months
        print(f"There are {number_months} months.")
        print(f"The total rainfall was {total:0.2f} inches.")
        print(f"The monthly average rainfall was {avg:0.2f} inches.")
                

        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
