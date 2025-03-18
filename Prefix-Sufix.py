def check_suffix_prefix(str1, str2):
    # Find the minimum length of both strings
    min_len = min(len(str1), len(str2))
    
    # Iterate from 1 to min_len to check for matching suffix and prefix
    for i in range(1, min_len + 1):
        if str1[-i:] == str2[:i]:  # Check if suffix of str1 matches prefix of str2
            return True  # Match found
    
    return False  # No match found

# Example Inputs
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# Check for suffix-prefix match
if check_suffix_prefix(string1, string2):
    print("Suffix of one string matches the prefix of the other.")
else:
    print("No match found.")