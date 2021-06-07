#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *
import decimal
a = 8
b = 9
x = f'seven {a:<09} {b:>09}'
print('x is {}'.format(x))
print(type(x))


a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

x = 1
print('x is {}'.format(x))
print(type(x))

if x:
    print(True)
else:
    print(False)
    
x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print('y is {}'.format(y))
print(type(x))
print(type(y))
print(id(x))
print(id(y))

if x[0] is y[0]:
    print('yep')
else:
    print('nope')
    
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('nope')