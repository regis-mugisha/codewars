def sum_of_intervals(intervals):
    sum = 0

    intervals.sort(key=lambda x: x[0])

    # merge overlapping intervals
    merged = [list(intervals[0])]

    for current_start, current_end in intervals[1:]:
        last_start, last_end = merged[-1]

        if current_start < last_end:
            merged[-1][1] = max(last_end, current_end)
        else:
            merged.append([current_start, current_end])

    for interval in merged:
        sum += interval[1] - interval[0]

    return sum
