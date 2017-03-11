#!/usr/bin/env python

## Given an index number, return the fibonaci sequencen up to that index.

def aar_fib(i):
    f = []
    for j in range(i + 1):
        if j in [0, 1]:
            f.append(j)
        else:
            f.append(f[j - 1] + f[j - 2])
    return f

## Given an index number, return the VALUE of the fibonaci sequence at that index number.

def aar_val(i):
    s = aar_fib(i)
    return s[-1]
