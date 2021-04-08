"""Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise"""
def is_multiple(number, multiplier):
    """this is a function that takes two numbers and does the check we need"""
    if multiplier <= 0:
        raise ValueError('multiplier be a positive non zero')
    return (number%multiplier) == 0

print(is_multiple(12, 3))
print(is_multiple(13, 0))
