"""
Input: a string with or without numbers
Output: number of characters that appear more than once

Steps:
- convert string to lowercase
- track frequency of characters in that string
- loop through the data structure tracking their frequencies
- if frequency > 1, increment count otherwise continue
- return count
"""


def duplicate_count(text):
    normalized_text = text.lower()
    freq_tracker = {}
    count = 0

    for char in normalized_text:
        if freq_tracker.get(char):
            freq_tracker[char] += 1
            if freq_tracker[char] == 2:
                count += 1
        else:
            freq_tracker[char] = 1

    print(count)
    return count


duplicate_count("aabBcde")
