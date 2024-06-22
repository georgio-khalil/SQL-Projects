"""
Author: Georgio Khalil, gkhalil@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/08/2022

Description:
    This program returns the days, hours, minutes, and seconds in a given duration in seconds.

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

    time = int(input("Please enter a time in seconds: "))

    if time <60:
        print(f"  {time} seconds is less than one minute.")
    else:
        d = time // 86400 #floor division of time by number of seconds in a day
        h = time % 86400 // 3600 #floor division of remaining seconds by nb of seconds in an hour 
        m = time % 3600 // 60
        s = time % 60
        print(f"  {time:,} seconds equals ", end = '')
        if d:
            print(f"{d} day(s)", end = '')
        if h:
            if d:
                if m or s:
                    print(', ', end='')
                else:
                    print(' and ', end='')
            print(f"{h} hour(s)", end = '')
        if m:
            if d or h:
                if s:
                    print(', ', end='')
                else:
                    print(' and ', end='')
            print(f"{m} minute(s)", end = '')
        if s:
            if d or h or m:
                print(' and ', end='')
            print(f"{s} second(s)", end = '')
        print('.')
    

        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
