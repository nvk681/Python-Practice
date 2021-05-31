def applyLimit(val):
    if val < -2147483648:
        val = -2147483648
    if val > 2147483647:
        val = 2147483647
    return val
def divide(dividend: int, divisor: int) -> int:
        sign = 1 if dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0 else -1
        dividend = applyLimit(dividend)
        divisor = applyLimit(divisor)
        dividend = dividend if dividend > 0 else -dividend
        divisor = divisor if divisor > 0 else -divisor
        value = 0
        if divisor == 1:
            result = applyLimit(sign*dividend)
            return result
        while dividend >= divisor:
            dividend -= divisor
            value += 1
        result = applyLimit(sign*value)
        return result

print(divide(10, 3))
print(divide(7, -3))
print(divide(0, 1))
print(divide(1, 1))