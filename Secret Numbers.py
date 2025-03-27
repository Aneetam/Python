def secret_message(s):
    words = s.lower().split()  # Convert to lowercase & split words
    converted_words = []  # Store processed words
    
    for word in words:
        secret_numbers = []  # Store numbers for each word
        for char in word:
            if char.isalpha():  # Ignore non-alphabet characters
                secret_numbers.append(str(ord(char) - ord('a') + 1))
        converted_words.append("-".join(secret_numbers))  # Join numbers with '-'
    
    return " ".join(converted_words)  # Join words with spaces

# Input from user
input_str = input().strip()
print(secret_message(input_str))