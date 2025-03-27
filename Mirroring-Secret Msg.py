def mirror_string(S):
    mirrored = ""
    for char in S:
        if char.isalpha():  # Check if it's a letter
            mirrored += chr(219 - ord(char)) if char.islower() else chr(155 - ord(char))
        else:
            mirrored += char  # Keep non-alphabet characters unchanged
    return mirrored
            
input_str = input().strip()
print(mirror_string(input_str))