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

final_matrix=[]
# Write your code here
for num in num_list:
    for row in num:
        final_matrix.append(row)
        
max_value=max(final_matrix)
min_value=min(final_matrix)
sum_value=sum(final_matrix)

print(max_value)
print(min_value)
print(sum_value)