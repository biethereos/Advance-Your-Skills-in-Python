#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = list(range(5))
x[3] = 42
for i in x:
    print('i is {}'.format(i))
    
    
x = (1, 2, 3, 4, 5)
# TypeError in tuple 
# x[3] = 42 immutable
for i in x:
    print('i is {}'.format(i))
    

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5}
x['three'] = 42
for k, v in x.items():
    print('k is {}, v is {}'.format(k, v))