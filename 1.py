from collections import Counter

def kth_most_frequent(s, k):
    # Count the frequency of each character
    char_count = Counter(s)

    # Sort the characters by their frequencies in descending order
    sorted_chars = sorted(char_count.keys(), key=lambda char: (-char_count[char], char))

    # Initialize a count to keep track of distinct characters
    count = 0

    for char in sorted_chars:
        if char_count[char] != char_count[sorted_chars[0]]:
            count += 1
        if count == k:
            return char

    return -1

# Input from the user
s = input("Enter a string: ")
k = int(input("Enter k: "))

result = kth_most_frequent(s, k)

if result == -1:
    print(f"There is no {k}-th most frequent character in the string.")
else:
    print(f"The {k}-th most frequent character in the string is: {result}")
