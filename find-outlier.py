def find_outlier(integers):

    if len(integers) < 3:
        return None

    first_three = integers[:3]
    even_majority = sum(n % 2 == 0 for n in first_three) >= 2

    for n in integers:
        if (n % 2 == 0) != even_majority:
            return n


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
