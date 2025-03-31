def reverseVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = list(s)  # Convert string to list for mutability
    l1, r = 0, len(s) - 1  # Two pointers

    while l1 < r:
        if s[l1] not in vowels:  # Move left pointer if not a vowel
            l1 += 1
        elif s[r] not in vowels:  # Move right pointer if not a vowel
            r -= 1
        else:  # Both s[l] and s[r] are vowels → Swap them
            s[l1], s[r] = s[r], s[l1]
            l1 += 1
            r -= 1

    return "".join(s)  # Convert list back to string

# Example test cases
print(reverseVowels("IceCreAm"))  # Output: "AceCreIm"
print(reverseVowels("leetcode"))  # Output: "leotcede"