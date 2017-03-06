#!/usr/bin/env python

def convert_base(x, new_base):
    ''' This function takes a base-10 number
    and a positive integer new_base >= 2 and
    prints out the number in base new_base. '''
    if new_base < 2:
        return "Nope"
    else:
        exp = 0
        res = x # This will serve as the 'residual' or what's left
        soln = '' # Initialization of the string that keeps track of our digits
        while new_base**exp <= x:
            exp = exp + 1 # Finding the left-most power of new_base that is relevant.
        for i in reversed(range(exp)):
            mult = 0 # Figure out what multiple to take each power to
            while (mult+1)*(new_base**i) <= res:
                mult = mult + 1 # Need to add 1 above to make sure mult doesn't go over.
            res = res - mult*(new_base**i) # Recompute the residual
            soln = soln + str(mult) # Add digits together as strings
        return int(soln) # Return converted back to integer
