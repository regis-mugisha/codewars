from itertools import combinations


def choose_best_sum(t, k, ls):
    possible_sums = [sum(combo) for combo in combinations(ls, k)]

    valid_sums = [s for s in possible_sums if s <= t]

    return max(valid_sums) if valid_sums else None


ts = [50, 55, 56, 57, 58]

print(choose_best_sum(163, 3, ts))
