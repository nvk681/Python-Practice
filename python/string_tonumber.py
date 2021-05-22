import numpy
def myAtoi(s: str) -> int:
        s = s.strip()
        list_of_items = numpy.array(list(s))
        if len(list_of_items) == 0:
            return 0
        sign = -1 if list_of_items[0] == '-' else 1
        if list_of_items[0] in ['+','-']:
            list_of_items = list_of_items[1::len(list_of_items)-1]
        parsed_list = []
        for item in list_of_items:
            if item.isdigit() == True:
                parsed_list.append(item)
            else:
                break
        del list_of_items
        if len(parsed_list) == 0:
            return 0
        number = 0
        while len(parsed_list) != 0:
            number = number*10+int(parsed_list.pop(0))
        number *= sign
        if number < -2147483648:
            number = -2147483648
        if number > 2147483647:
            number = 2147483647
        return number

print(myAtoi(""))
print(myAtoi("42"))
print(myAtoi("   -42"))
print(myAtoi("-42"))
print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("-91283472332"))