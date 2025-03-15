num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
N=int(input())
result=[]
for num in num_list:
    filtered_tuple=tuple(x for x in num if x!=N)
    result.append(filtered_tuple)

print(result)