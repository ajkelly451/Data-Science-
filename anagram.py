#!/usr/bin/env python

##

from itertools import combinations

def ana_duple(a):
    ''' Given a list of strings, this function will return
    an embedded dictionary of anagram duples.
    For example, ['bob', 'ana', 'ann', 'cat', 'obb', 'nan']
    will return {'bbo': [0, 4], 'ann': [[1,2], [1,5], [2,5]]} '''
    # Create new list to populate with the strings sorted
    # by character.
    b = []
    for i, val in enumerate(a):
        b.append(''.join(sorted(val)))
    # Create and populate dictionary keeping track of all
    # indeces that map to each sorted string.
    c = {}
    for i, val in enumerate(b):
        if val not in c.keys():
            c[val] = [i] # Initilize index at that key.
        else:
            c[val].append(i) # Append if key already present.
    # For each ordered string, return all combinations of indeces
    # That are 2 indeces long.
    for i in c.keys():
        c[i] = [map(str, comb) for comb in combinations(c[i], 2)]
    return(c)
