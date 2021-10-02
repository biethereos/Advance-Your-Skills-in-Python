# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    '''MyFunction(arg1, arg2=None) --> doesn't really do anything, just print.
    
    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: second argument. Default to None. 
    '''
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
