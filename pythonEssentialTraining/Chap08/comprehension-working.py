#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
def main():
    seq = range(11)
    # print_list(seq)
    # seq2 = [x * 2 for x in range(11)]
    # seq2 = [x for x in seq if x % 3 != 0]
    # seq2 = [(x, x ** 2) for x in seq]
    # from math import pi
    # seq2 = [round(pi, i) for i in seq]
    # seq2 = {x : x ** 2 for x in seq}
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print(seq2)
    
    print_list(seq2)
    
def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
