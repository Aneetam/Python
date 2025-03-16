def replace_old_value_with_new_value(matrix, old_value, new_value):
    # Complete this function
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==old_value:
                matrix[i][j]=new_value


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

values = input().split()
old_value, new_value = convert_string_to_int(values)

# Call the replace_old_value_with_new_value function
replace_old_value_with_new_value(num_list,old_value,new_value)
# Write your code here
for row in num_list:
    print(row)