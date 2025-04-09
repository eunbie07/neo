#!/usr/bin/env python

def division_funciton(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('First')
    except TypeError as e:
        print('Second')
    except ZeroDivisionError as e:
        print('Third')

division_funciton("a", 1)
division_funciton(1, 0)
division_funciton(4, 2)