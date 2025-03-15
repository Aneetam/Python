num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]

N = int(input())

# Iterate through each tuple, remove N, and update the tuple
for i in range(len(num_list)):
    num_set = set(num_list[i])
    num_set.discard(N)
    num_list[i] = tuple(num for num in num_list[i] if num in num_set)

print(num_list)