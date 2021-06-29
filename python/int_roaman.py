def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roam = ''
        i = 0
        while  num > 0:
            for k in range(num // val[i]):
                roam += syb[i]
                num -= val[i]
            i += 1
        return roam