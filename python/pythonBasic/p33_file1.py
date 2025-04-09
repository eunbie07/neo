#!/usr/bin/env python

f = open('text.txt')
line = 1
while line:
    line = f.readline()
    print(line)
f.close()
