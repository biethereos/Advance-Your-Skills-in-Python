#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
# l = s.split('i')
l = s.split()
# s2 = ':'.join(l)
s2 = '--'.join(l)
print(s2)
