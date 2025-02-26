def shuffle_string(s, indices):
    return ''.join(s[i] for i in indices)

# Read input
s = input().strip()
indices = list(map(int, input().split()))

# Get the shuffled string
result = shuffle_string(s, indices)

# Print the output
print(result)