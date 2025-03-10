def mergeAlternately( word1, word2):
    merge = []
    len1, len2 = len(word1), len(word2)
    min_len = min(len1, len2)

        # Merge characters alternatively
    for i in range(min_len):
        merge.append(word1[i])
        merge.append(word2[i])

        # Append remaining characters (if any)
    if len1 > len2:
        merge.extend(word1[min_len:])  # Correctly appending remaining characters
    elif len2 > len1:
        merge.extend(word2[min_len:])

    return "".join(merge)  # Convert list to string

# Input values
word1 = input().strip()
word2 = input().strip()

# Create an instance of Solution and call the function

print(mergeAlternately(word1, word2))