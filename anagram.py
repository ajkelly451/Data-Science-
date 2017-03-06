#!/usr/bin/env python

## Given a list of strings, return an embedded list of anagram duples.

from itertools import combinations

def ana_duple(a):
    b = []
    for i, val in enumerate(a):
        b.append(''.join(sorted(val)))
    c = {}
    for i, val in enumerate(b):
        if val not in c.keys():
            c[val] = [i]
        else:
            c[val].append(i)
    for i in c.keys():
        c[i] = [map(str, comb) for comb in combinations(c[i], 2)]
    return(c)
