#!/usr/bin/env python

import random

def fingMax(data):
    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max

data = random.sample(range(101), 10)
print(data)
print(f'Max value is {fingMax(data)}')



