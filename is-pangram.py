import string

# Quick solution

# def is_pangram(st):
#     lowercase_trimmed_str = st.lower().replace(" ", "")

#     alphabet_freq = {char: 0 for char in string.ascii_lowercase}

#     for char in lowercase_trimmed_str:
#         if char in alphabet_freq:
#             alphabet_freq[char] += 1

#     return all(freq > 0 for freq in alphabet_freq.values())


# Optimized solution
def is_pangram(st):
    letters = set(char.lower() for char in st if char.isalpha())
    return set(string.ascii_lowercase).issubset(letters)


print(is_pangram("The quick brown fox jumps over the lazy dog."))
