"""Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function"""
def sum_of_odd_squares(value):
    """A function to calculate the sum"""
    return sum([k*k for k in range(1, value, 2)])

number = int(input("Please enter a number: "))
print(sum_of_odd_squares(number))
