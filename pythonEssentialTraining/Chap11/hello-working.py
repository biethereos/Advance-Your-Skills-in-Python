#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World. {}'.format(42 * 7))
print('''
         Hello,
         World. 
      
      
      
      
      {}'''.format(42 * 7))

s = 'Hello, World. {}'
print(s.format(42 * 7))

class myString(str):
    def __str__(self):
        return self[::-1]


s = myString('Hello, World.')
print(s)
print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World. straße'.casefold())

s1 = 'Hello, World'
# s2 = s1.upper()
s2 = 'this is another string'

# print(id(s1))
# print(id(s2))
print(s1 + ' ' + s2)

s3 = 'this string' ' that string'
print(s3)

x = 42 
y = 73
print('the number is {xx} {bb}'.format(xx = x, bb = y))
print('the number is {bb} {xx}'.format(xx = x, bb = y))
print('the number is {1} {0}'.format(x, y))
print('the number is {1} {0} {0}'.format(x, y))
print('the number is {} {}'.format(x, y))
print('the number is {0:<5} {1:>5}'.format(x, y))
print('the number is {0:<5} {1:>05}'.format(x, y))
print('the number is {0:<5} {1:+05}'.format(x, y))

z = 43 * 747 * 1000
print('the number is {:,}'.format(z))
print('the number is {:,}'.format(z).replace(',', '.'))
print('the number is {:f}'.format(z))
print('the number is {:.3f}'.format(z))

print('the number is {:x}'.format(x))
print('the number is {:o}'.format(x))
print('the number is {:b}'.format(x))

print(f'the number is {x:.3f}')



