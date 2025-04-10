#!/usr/bin/env python

import random

class BinaryConverter:
    def __init__(self, num=None):
        self.num = num if num is not None else random.randrange(4, 20)
        self.binarydigits = []

    def convert(self):
        self.binarydigits = []
        self.re_convert(self.num)
        return self.binarydigits

    def re_convert(self, num):
        q = num // 2
        r = num % 2
        self.binarydigits.append(r)
        if q == 0:
            self.binarydigits.reverse()
        else:
            self.re_convert(q)

    def display(self):
        binary = self.convert()
        print(f'{self.num} binary number is: {binary}')


converter = BinaryConverter()
converter.display()
