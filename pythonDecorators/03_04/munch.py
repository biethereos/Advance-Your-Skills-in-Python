from functools import wraps


def munch(start, end):
    def do_munch(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_string = ''
            result = func(*args, **kwargs)
            for i, c in enumerate(result):
                c = 'x' if start <= i < end else c
                new_string += c
            return new_string
        return wrapper
    return do_munch


@munch(1, 4)
def fib():
    return 'Fibonacci'


print(fib())
