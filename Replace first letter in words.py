def replace_first_letter(s):
    words = s.split()  # Split sentence into words
    modified_words = []

    for word in words:
        if word[0].isalpha():  # Check if first character is a letter
            new_first_letter = chr(ord(word[0]) + 1)  # Get next letter
            modified_words.append(new_first_letter + word[1:])  # Replace first letter
        else:
            modified_words.append(word)  # Keep unchanged if first char is not a letter

    return " ".join(modified_words)  # Join words back into a sentence

# Example Usage
S = "East And West"
print(replace_first_letter(S))  
# Output: "Ifmmp Afcsb! Bpple qie."