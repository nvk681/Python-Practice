def romanToInt(s: str) -> int:
        if len(s) <1 or len(s) >15:
            return 0
        map_of_value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        i = 0
        while (i < len(s)):
            last_sum = map_of_value[s[i]]
            if (i + 1 < len(s)):
                sum = map_of_value[s[i + 1]]
                if (last_sum >= sum):
                    res = res + last_sum
                    i = i + 1
                else:
                    res = res + sum - last_sum
                    i = i + 2
            else:
                res = res + last_sum
                i = i + 1
        return res

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))