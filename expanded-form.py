def expanded_form(num):
    if num <= 0:
        return "Number should be greater than 0"

    res = []
    num_str = str(num)

    length = len(num_str)
    if length == 1:
        return num_str

    for i in range(1, length + 1):
        if int(num_str[i - 1]) != 0:
            expanded_chunk = int(num_str[i - 1]) * pow(10, length - i)
            res.append(expanded_chunk)

    res_str = list(map(str, res))
    return " + ".join(res_str)


print(expanded_form(45))
print(expanded_form(70304))
