#!/usr/bin/env python

n = 1
numbers = [1,2]
print(numbers)



s4 = {6, 7, 8, 9, 10}

s2 = {4, 5}

s5 = {4, 5}

print(s4)

print(s5.issubset(s2))

s = {1, 2, 3}
print(f'set : {s}')

s.update({'a', 'b', 'c'})
print(f'set : {s}')

s.update(([11,12,13]))
print(f'set : {s}')

s.remove('a')
print(f'set : {s}')

s.discard('d')
print(f'set : {s}')

a = {'r', 'd', 'n', 'd', 'o', 'm'}
print(f'set : {a}')


