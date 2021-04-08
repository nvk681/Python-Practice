"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n"""
def get_sum_of_squares(number):
    """Function to get the sum"""
    total = 0
    for item in range(number):
        total += item**2
    return total

number = int(input("please enter a number: "))
print(get_sum_of_squares(number))
