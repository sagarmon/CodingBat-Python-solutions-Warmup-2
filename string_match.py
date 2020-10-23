'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''

def string_match(a, b):
    result = 0
    for i in range(len(a) - 1):
        if a[i:i + 2] == b[i:i + 2]:
            result += 1
    return result
