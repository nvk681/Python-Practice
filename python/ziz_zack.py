def convert(s: str, numRows: int) -> str:
    if numRows==1:
        return s
    string_length = len(s)
    zig_zach_list = []
    for index in range(numRows):
        zig_zach_list.append([""]*string_length)
    character_items = list(s)
    del s
    field = 0
    while len(character_items) != 0:
        for index in range(numRows):
            if len(character_items) != 0:
                zig_zach_list[index][field] = character_items.pop(0)
        paused_index, field = numRows-2, field+1
        while paused_index > 0 and len(character_items) != 0:
            zig_zach_list[paused_index][field] = character_items.pop(0)
            paused_index, field = paused_index-1, field+1
    del paused_index
    del field
    del character_items
    parsed_string = [];
    for row in zig_zach_list:
        for item in row:
            if item != "":
                parsed_string.append(item)
    output = ""
    output = output.join(parsed_string)
    del parsed_string
    return output

print("PAHNAPLSIIGYIR" == convert("PAYPALISHIRING", 3))
print("PINALSIGYAHRPI" == convert("PAYPALISHIRING", 4))
print("A" == convert("A", 1))
