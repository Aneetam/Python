def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

# Reading input and converting to integers
for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Finding the maximum element and its position
max_val = float('-inf')
max_row, max_col = -1, -1

for i in range(m):
    for j in range(n):
        if num_list[i][j] > max_val:
            max_val = num_list[i][j]
            max_row, max_col = i, j

# Printing the row with the maximum element
print("Row:", *num_list[max_row])

# Printing the column with the maximum element
print("Column:", end=" ")
for i in range(m):
    print(num_list[i][max_col], end=" ")