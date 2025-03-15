list_a = [('apple', 'banana', 'orange', 'grapes'),
          ('cricket', 'football', 'hockey'),
          ('car', 'bicycle', 'bus')]

# Input number of queries
N = int(input())

# Initialize an empty list to store results
result = []

# Loop through each query
for _ in range(N):
    # Read indices
    tuple_index, value_index = map(int, input().split())
    # Access and append the value to result list
    result.append(list_a[tuple_index][value_index])

# Print the result as a single line
print(result)