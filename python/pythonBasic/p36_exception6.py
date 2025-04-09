#!/usr/bin/env python

def division_funciton(a, b):
    try:
        print(a / b)
    except TypeError as e:
        return -1
    except ZeroDivisionError as e:
        return -2
    except Exception as e:
        return -3

ret = division_funciton("a", 1)
print(ret)
ret = division_funciton(1, 0)
print(ret)
ret = division_funciton(4, 2)
if ret != None:
    print('Error')
