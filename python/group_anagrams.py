def groupAnagrams(strs):
        my_list = {}
        for i in strs:
            sorted_characters = sorted(i)
            j = "".join(sorted_characters)
            if j not in my_list:
                my_list[j] = [i]
            else:
                my_list[j].append(i)
        result = []
        for i in my_list:
            result.append(my_list[i])
        return result

# groupAnagrams(["eat","tea","tan","ate","nat","bat"])
groupAnagrams([""])
groupAnagrams(["eat"])