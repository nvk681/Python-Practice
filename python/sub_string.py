def lengthOfLongestSubstring(s: str) -> int:
        list_of_characters = list(s)
        max = 1 if len(list_of_characters) > 0 else 0
        for index in range(len(list_of_characters)):
            current_list = [list_of_characters[index]]
            current_max = 1
            for sub_index in range(index+1, len(list_of_characters)):
                if list_of_characters[sub_index] not in current_list:
                    current_max += 1
                    max = current_max if current_max > max else max
                    current_list.append(list_of_characters[sub_index])
                else:
                    break
        return max

print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))