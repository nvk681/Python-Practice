check_if_square_root = lambda element : (element == ((int(element**0.5))**2))
for iterations in range(int(input())):
    limits = list(map(lambda variable : int(variable), input().split()))
    count_of_roots = 0
    for current_element in range(limits[0], (limits[1]+1)):
        if check_if_square_root(current_element):
            count_of_roots+=1
    print(count_of_roots)
