def trap(height) -> int:
        next_max = list()
        if len(height) == 0 or len(height) == 1:
            return 0
        for index in range(0, len(height)):
            current_min = None
            if index < (len(height)-1):
                for sub_index in range(index+1, len(height)):
                    if height[sub_index] > height[index] and (current_min is None or current_min < height[sub_index]):
                        current_min = height[sub_index]
            next_max.append(current_min)
        previous_max = None
        total = 0
        for index in range(len(height)):
            next_max_value = next_max[index]
            if previous_max is None:
                previous_max = height[index]
                continue
            if next_max_value is None:
                if previous_max < height[index]:
                    previous_max = height[index]
                continue
            min_of_two = min(previous_max, next_max_value)
            if min_of_two > height[index]:
                total += min_of_two - height[index]
            if previous_max < height[index]:
                previous_max = height[index]

        return total

print(6 == trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(9 == trap([4,2,0,3,2,5]))
print(23 == trap([5,5,1,7,1,1,5,2,7,6]))