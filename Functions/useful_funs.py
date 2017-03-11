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

def median(x):
    ''' This function takes a list of numerical values
    and returns its median. For large lists too large to
    be stored in memory, the binned estimation below may
    work. '''
    l = len(x) # get length so it doesn't have to be repeatedly returned
    # Create hash table
    h = {}
    for i in x:
        if i not in h.keys():
            h[i] = 1 # Initialize counts for this int
        else:
            h[i] = h[i] + 1 # Add one for ints already in table
    # This part iterates through to find which integer is in the middle
    count = 0
    for j in sorted(h.keys()): # Sorting the keys is essential here.
        if count >= l//2:
            if count == l/2:
                med = (med + j)/2 # Calculates between indices if we have even-sized list.
                break
            else:
                break
        count = count + h[j]
        med = j
    return med

def median_binned(x, bins, method='medians'):
    ''' This function is a wrapper around
    the above function. It takes in 
