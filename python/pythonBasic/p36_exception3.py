#!/usr/bin/env python

def division_funciton(a, b):
    try:
        print(a/b)
    except TypeError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

division_funciton("a", 1)
division_funciton(1, 0)
division_funciton(4, 2)