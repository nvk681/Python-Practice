def is_palindrome(text):
    lenght = len(text)
    for index in range(0, lenght//2):
        if text[index] != text[lenght - 1 - index]:
            return False
    return True
    
    def longestPalindrome(s: str) -> str:
        list_of_characters = list(s)
        max_len = 1 if len(s) > 0 else 0
        max_string = s[0] if len(s) > 0 else ""
        for index in range(len(list_of_characters)):
            for sub_index in range(index, len(list_of_characters)):
                if is_palindrome(list_of_characters[index:sub_index+1]) and max_len < (sub_index - index + 1):
                    max_len = (sub_index - index + 1)
                    max_string = s[index:sub_index+1]
        return max_string
    
print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("a"))
print(longestPalindrome("ac"))