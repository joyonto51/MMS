def triplet_masker(s, d):
    ln = len(s)
    start = 0
    output = ""

    for end in range(3, ln+1, 3):
        item = s[start:end]
        start = end

        if item in d:
            value = d[item]
            output += "{}".format(value)
        else:
            output += "¿"

    print(output)


mask_dict = {"abc": 1, "def": 2, "ghi": 3}
inp_str = "mnj999abcpladef"

triplet_masker(inp_str, mask_dict)