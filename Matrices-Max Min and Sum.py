def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    transpose=[]
    for j in range(n):
        row=[]
        for i in range(m):
            row.append(matrix[i][j])
        transpose.append(row)
    return transpose


def print_max_min_sum_for_row_wise(num_list):
    # Complete this function
    max_value=[max(row) for row in num_list]
    min_value=[min(row) for row in num_list]
    sum_value=[sum(row) for row in num_list]
    print(max_value)
    print(min_value)
    print(sum_value)


def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


# Write your code here
# Call the get_transpose_of_matrix function
transpose=get_transpose_of_matrix(num_list,m,n)
# Call the print_max_min_sum_for_row_wise function
print_max_min_sum_for_row_wise(transpose)