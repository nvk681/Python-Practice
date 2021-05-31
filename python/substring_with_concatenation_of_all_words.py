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
    for item in words:
        length_of_each_word[item] = len(item)
    