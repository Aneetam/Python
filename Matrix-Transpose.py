def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    transpose=[]
    for j in range(n):
        new_row=[]
        for i in range(m):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    return transpose
        

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

# Call the get_transpose_of_matrix function
transpose=get_transpose_of_matrix(num_list,m,n)
for row in transpose:
    print(row)