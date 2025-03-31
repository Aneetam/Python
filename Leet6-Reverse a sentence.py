def reverseWords(s):
    return ' '.join(s.strip().split()[::-1])

# Taking input from the user
s = input("Enter a sentence: ")

# Calling the function and printing the result
print("Reversed words:", reverseWords(s))