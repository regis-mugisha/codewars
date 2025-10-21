import string


def rot13(message):
    res = ""
    if not message:
        return res

    for char in message:
        if char.isalpha():
            if char.isupper():
                pos = string.ascii_uppercase.index(char)
                rot13_char = string.ascii_uppercase[(pos + 13) % 26]
                res += rot13_char
            else:
                pos = string.ascii_lowercase.index(char)
                rot13_char = string.ascii_lowercase[(pos + 13) % 26]
                res += rot13_char
        else:
            res += char

    return res


print(rot13("test"))
