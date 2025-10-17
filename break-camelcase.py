def solution(s):
    if len(s) == 0:
        return ""

    res = ""

    for char in s:
        if char.isupper():
            res += " "
        res += char

    return res


print(solution("breakCamel Case"))
