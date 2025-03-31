from math import gcd  # Import gcd function from math module

def gcdOfStrings(str1: str, str2: str) -> str:
    # Check if str1 and str2 have a common divisor pattern
    if str1 + str2 != str2 + str1:
        return ""  # No common divisor exists, return empty string
    
    # Find the greatest common divisor of the lengths of str1 and str2
    gcd_length = gcd(len(str1), len(str2))
    
    # The largest common divisor string is the first gcd_length characters of str1
    return str1[:gcd_length]

# Taking input from the user
input1 = input()
input2 = input()

# Calling the function and printing the result
result = gcdOfStrings(input1, input2)
print("Output:", result)