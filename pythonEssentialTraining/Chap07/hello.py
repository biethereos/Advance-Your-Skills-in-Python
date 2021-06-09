#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def f1():
#     print('this is f1')

def f1(f):
    def f2():
        print('this is befor function call')
        f()
        print('this is after function call')
    return f2

# x = f1()
# x()
# x = f1(f3)
# x()
# f3 = f1(f3)
# f3()

@f1
def f3():
    print('this is f3')
    
f3()
