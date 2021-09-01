'''
Fixed arguments
'''


def pfib(a, b, c):
    print(a, b, c)


pfib(1, 1, 2)

# pfib(1, 1, 2, 3)

'''
Using *args
'''


def pfib(a, *args):
    print(a)
    print(args)

pfib(1, 1, 2, 3)


pfib(1)

'''
Using **kwargs
'''


def pfib(a, **kwargs):
    print(a)
    print(kwargs)


pfib(1, se=1, th=2, fo=3, fi=5)

pfib(1)

'''
Using *args and **kwargs
'''


def pfib(*args, **kwargs):
    print(args)
    print(kwargs)


pfib(1, 1, 2, 3)

pfib(fi=1, se=1, th=2, fo=3)

pfib(1, 1, 2, fo=3, fi=5)

pfib()


def wrapper(*args, **kwargs):
    print(args)
    print('Leaving wrapper')
    pfib(*args, **kwargs)


wrapper(1, 1, th=2)
