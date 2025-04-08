#!/usr/bin/env python

import datetime

def datetime_deco(func):
    def docorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
        print()
    return docorated

@datetime_deco
def func1():
    print('Main Function start')

@datetime_deco
def func2():
    print('Main Function start')

@datetime_deco
def func3():
    print('Main Function start')

func1()
func2()
func3()
