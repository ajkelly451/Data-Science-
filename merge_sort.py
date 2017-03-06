#!/usr/bin/env python

def sort_sorted(a, b):
    if not b:
        return a
    else:
        c = []
        for i in b:
            while a:
                if i > a[0]:
                    c.append(a[0])
                    a = a[1:]
                else:
                    break
            c.append(i)
        return c + a

def merge_sort(a):
    a = a.tolist()
    if len(a) < 2:
        return a
    else:
        ind = len(a)//2
        x = merge_sort(a[:ind])
        y = merge_sort(a[ind:])
        return sort_sorted(x, y)
