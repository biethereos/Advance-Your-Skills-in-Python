
def pfib(*args, **kwargs):
    print(args)
    print(kwargs)

def wrapper(*args, **kwargs):
    print('In wrapper ... unpacking args')
    print(*args)
    pfib(*args, **kwargs)

wrapper(1, 1, th=2)