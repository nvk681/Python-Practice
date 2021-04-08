"""Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function"""
def get_sum_of_squares(number):
    """Function to get the sum"""
    return sum([k*k for k in range(1, number)])

number = int(input("please enter a number: "))
print(get_sum_of_squares(number))
