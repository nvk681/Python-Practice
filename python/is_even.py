"""Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators"""
def is_even(number):
    """Function to do the check and we treat a zero as an even number"""
    if number == 0:
        return True
    while number not in (0, 1):
        number -= 2
    if number == 0:
        return True
    return False

print(is_even(0))
print(is_even(1))
print(is_even(2))
