"""Finding Euclidean norm of a list of numbers
input type list of number followed by the power"""
def euclidean_norm(list_of_items, power):
    """A function to calculate the euclidean norm"""
    total = 0
    for item in list_of_items:
        total += int(item)**power
    return total**(1./power)
list_of_numbers = list(map(int, input("\nEnter the numbers : ").strip().split()))
power = int(input("Enter the power: "))
print(euclidean_norm(list_of_numbers, power))
