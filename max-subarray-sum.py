"""
🧠 1. What is Kadane’s Algorithm?

Kadane’s Algorithm is a fast way to find the maximum sum of a contiguous subarray in a list of integers (positive, negative, or mixed).

⚙️ 5. How does it work?

Here’s the step-by-step idea:

We track two things:

current_sum — the sum of the current subarray we’re building.

max_sum — the best sum we’ve found so far.

Algorithm steps:

Start both at 0
(current_sum = 0, max_sum = 0)

For each number in the array:

Add it to current_sum

If current_sum becomes negative, reset it to 0
(because continuing a negative sum will only make things worse)

Update max_sum if current_sum is bigger than before

Return max_sum at the end.

"""


def max_sequence(arr):
    current_sum = 0
    max_sum = 0

    if not arr:
        return max_sum

    for item in arr:
        current_sum += item

        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)

    return max_sum
