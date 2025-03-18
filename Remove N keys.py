alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

# Write your code here
key_list=input().split()
for key in key_list:
    if key in alphabets.keys():
        del alphabets[key]
print(alphabets)