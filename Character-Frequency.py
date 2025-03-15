def character_frequency(text):
    # Convert text to lowercase and remove spaces
    text = text.replace(" ", "").lower()
    
    # Create a list of unique characters (ignoring duplicates)
    unique_chars = []
    for char in text:
        if char not in unique_chars:
            unique_chars.append(char)
    
    # Count the frequency of each unique character
    result = []
    for char in sorted(unique_chars):
        count = 0
        for c in text:
            if c == char:
                count += 1
        result.append((char, count))
    
    return result

# Taking input from the user
text = input("Enter a string: ")

# Calculating character frequency
result = character_frequency(text)

# Printing the result
for char, count in result:
    print(f"{char}: {count}")