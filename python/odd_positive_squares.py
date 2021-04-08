"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n"""
def sum_of_odd_squares(value):
    """A function to calculate the sum"""
    total = 0
    for item in range(1, value, 2):
        total += item**2
    return total
number = int(input("Please enter a number: "))
print(sum_of_odd_squares(number))
