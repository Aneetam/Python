tuple_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
N=int(input())
updated_list=[]
for t in tuple_list:
    without_last=t[:-1]
    new_tuple=without_last+(N,)
    updated_list.append(new_tuple)
print(updated_list)