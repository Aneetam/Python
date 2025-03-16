def print_max_min_sum_for_row_wise(num_list):
    # Complete this function
    max_value=[]
    min_value=[]
    sum_value=[]
    for num in num_list:
        max_value.append(max(num))
        min_value.append(min(num))
        sum_value.append(sum(num))
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

print_max_min_sum_for_row_wise(num_list)