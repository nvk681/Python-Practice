"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution"""
def minmax(list_of_numbers):
    """A function to find and return the min and max"""
    if not bool(list_of_numbers):
        return "Empty list"
    min = max = list_of_numbers[0]
    for item in list_of_numbers:
        if item < min:
            min = item
        if item > max:
            max = item
    return min, max

print(minmax([1, 2, 3]))
print(minmax([3, 4, 4]))
print(minmax([]))
