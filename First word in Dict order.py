def first_word_in_order(s):
    words = s.split()  # Split sentence into words
    return min(words, key=str.lower)  # Find the first word ignoring case

# Example usage
S = "Zebra mango Kiwi apple"
print(first_word_in_order(S))  # Output: apple

S = "Banana orange Apple grape"
print(first_word_in_order(S))  # Output: Apple