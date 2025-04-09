#!/usr/bin/env python

def division_funciton(a, b):
    try:
        print(a / b)
    except TypeError as e:
        print('First')
    except ZeroDivisionError as e:
        print('Second')
    except Exception as e:
        print('Third')


division_funciton("a", 1)
division_funciton(1, 0)
division_funciton(4, 2)
