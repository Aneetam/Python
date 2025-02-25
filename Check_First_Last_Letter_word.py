words = input().split()  # Read input and split into words

for word in words:
    if word[0].lower() == word[-1].lower():  # Compare first and last letter (case-insensitive)
        print(True)
    else:
        print(False)