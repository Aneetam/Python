def add_two_matrices(first_matrix, second_matrix, m, n):
    # Initialize the final matrix with zeros
    final_matrix = []

    # Iterate through rows and columns to add elements
    for i in range(m):
        row = []
        for j in range(n):
            row.append(first_matrix[i][j] + second_matrix[i][j])
        final_matrix.append(row)
    
    return final_matrix


def convert_string_to_int(list_a):
    return [int(item) for item in list_a]


def read_matrix_inputs(m):
    num_list = []
    for _ in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


# Input for number of rows and columns
m, n = map(int, input().split())

# Reading the two matrices
first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)

# Adding the two matrices
result = add_two_matrices(first_matrix, second_matrix, m, n)

# Printing the result
for row in result:
    print(row)