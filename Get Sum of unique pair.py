# Input from the user
numbers = list(map(int, input("Enter comma-separated integers: ").split(",")))
K = int(input("Enter the target sum (K): "))

# Using a set to store unique pairs
unique_pairs = set()

# Iterate through the list to find pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == K:
            # Store the pair as a tuple in sorted order to avoid duplicates
            unique_pairs.add(tuple(sorted((numbers[i], numbers[j]))))

# Convert the set to a sorted list of pairs
result = sorted(unique_pairs)

# Print the result
print(result)