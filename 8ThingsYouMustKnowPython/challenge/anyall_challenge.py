import string


def contains_punctuation(input_str):
    ''' Return True if the input_str contains punctuations.
    Return False otherwise'''
    # for char in input_str:
    #     if char in string.punctuation:
    #         return True
    # return False
    # Replace this line with your solution
    return any(
        char in string.punctuation
        for char in input_str
    )
