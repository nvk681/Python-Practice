from itertools import combinations

def check_sum(numbers, total):
    list_of_sets = []
    for r in range(len(numbers)):
        for combo in combinations(numbers, r + 1):
            if sum(combo) == total:
                list_of_sets.append(combo)
    return list_of_sets

def find_combinations(numbers, total):
        total_set = []
        for index in range(len(numbers)):
            current_sum = numbers[index]
            current_set = [numbers[index]]
            if total == current_sum:
                total_set.append(current_set)
            while total > current_sum:
                current_sets = check_sum(numbers, total-current_sum)
                for current in current_sets:
                    temp = list(current_set)
                    for i in current:
                        temp.append(i)
                    total_set.append(temp)
                current_set.append(numbers[index])
                current_sum += numbers[index]
        total_set.sort()
        for index in range(len(total_set)):
            if index+1 < len(total_set) and sorted(total_set[index]) == sorted(total_set[index+1]):
                total_set.pop(index)
        return total_set 

# find_combinations([2,3,6,7], 7)
find_combinations([2,7,6,3,5,1], 9)