"""
Steps:
- initialize array
- loop through the sequence
- add sequence item our array
- if next item is similar to previous one skip it
- return array
"""


def unique_in_order(sequence):
    arr = []

    if len(sequence) == 0:
        return arr

    arr.append(sequence[0])

    for i in range(1, len(sequence)):
        prev = sequence[i - 1]
        next = sequence[i]
        if next != prev:
            arr.append(next)
    return arr
