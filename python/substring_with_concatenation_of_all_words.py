def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def strStr(haystack: str, needle: str):
        if not needle:
            return 0
        if not haystack:
            return -1
        for index in range(len(haystack)-len(needle)+1):
            for sub_index in range(len(needle)):
                if haystack[index+sub_index]!=needle[sub_index]:
                    break
            else:
                return index
        else:
            return -1

def findSubstring(string, words):
        length_of_each_word = {}
        list_of_index = {}
        return_value = []
        for item in words:
            length_of_each_word[item] = len(item)
            list_of_index[item] = []
        
        for current_word in words:
            temp_string = string
            index = strStr(temp_string, current_word)
            last_index = None
            while index != -1 :
                if last_index is None:
                    list_of_index[current_word].append(index)
                else:
                    list_of_index[current_word].append(last_index+index+1)
                
                if index < len(temp_string):
                    if last_index is None:
                        last_index = index
                    else:
                        last_index = last_index+index+1
                    temp_string = temp_string[index+1::]
                    index = strStr(temp_string, current_word)
        for item in list_of_index:
            if len(list_of_index[item]) == 0:
                return return_value
            res = []
            for i in list_of_index[item]:
                if i not in res:
                    res.append(i)
            list_of_index[item] = res
        if len(words) == 1:
            return list_of_index[words[0]]

        for item in words:
            selected_list = list_of_index[item]
            for start in selected_list:
                end = []
                temp_selection = [item]
                end.append(start+length_of_each_word[item])
                for i in range(len(words)-1):
                    for next_item in words:
                        if countX(temp_selection, next_item) != countX(words, next_item):
                            mid_points = intersection(end, list_of_index[next_item])
                            if len(mid_points) != 0:
                                temp_selection.append(next_item)
                                new_end = []
                                for addition in end:
                                    new_end.append(addition+length_of_each_word[next_item])
                                end = new_end
                    if len(words) == len(temp_selection):
                        temp_selection = []
                        return_value.append(start)
        res = []
        for i in return_value:
            if i not in res:
                res.append(i)
        return res

a = findSubstring("mississippi", ["is"])
print(a)
# a = findSubstring("a", ["a"])
# print(a)
# a = findSubstring("barfoothefoobarman", ["foo","bar"])
# print(a)
# a = findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])
# print(a)
# a = findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])
# print(a)
# a = findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
# print(a)