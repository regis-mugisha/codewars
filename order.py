def order(sentence):
    if len(sentence) == 0:
        return ""

    text_split = sentence.split()
    size = len(text_split)
    arr_sort = [0] * size

    for word in text_split:
        for char in word:
            if char.isdigit():
                arr_sort[int(char) - 1] = word

    return " ".join(arr_sort)


print(order("is2 Thi1s T4est 3a"))
