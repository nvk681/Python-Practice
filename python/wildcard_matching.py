def isMatch( s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '?', '*'}

        if len(p) >= 2 and p[1] == '*':
            return first_match and isMatch(s[1:], p)
        else:
            return first_match and isMatch(s[1:], p[1:])

print(isMatch("aa", "a"))
print(isMatch("aa", "*"))
print(isMatch("cb", "?a"))
print(isMatch("adceb", "a*b"))
print(isMatch("adceb", "a*c?b"))
# print(isMatch("aa", "a"))
# print(isMatch("aa", "a"))