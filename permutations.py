import itertools


def permutations(s):
    possible_combinations = list(
        set("".join(perm) for perm in itertools.permutations(s, len(s)))
    )

    return possible_combinations


print(permutations("a"))
