"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/08/2022

Description:
    This program calculates Reynolds number based on given velocity, diameter, and water temperature.

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
    #gathering inputs
    T = float(input("Enter the temperature in \u00B0C as 5, 20, or 50: "))
    V = float(input("Enter the velocity of water in the pipe (m/s): "))
    d = float(input("Enter the pipe's diameter (m): "))

    #determining kinematic viscosity
    if T == 5:
        v = 1.52 * (10**-6)
    if T == 20:
        v = 10**-6
    if T == 50:
        v = 5.54 * (10**-7)

    #calculating Reynolds number
    Re = (V*d/v)

    print(f"At {T:.1f}\u00B0C, the Reynolds number for flow at {V} m/s in a {d} m diameter pipe is {Re:.2e}.")
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
