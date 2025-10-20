def in_array(array1, array2):

    substring_array = []

    for substring in array1:
        for main_string in array2:
            if substring in main_string:
                substring_array.append(substring)
                break

    return sorted(substring_array)
