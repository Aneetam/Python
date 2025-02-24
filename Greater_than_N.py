num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
N=int(input())
new_num_list=[]
for num in num_list:
    if num>N:
        new_num_list+=[num]
print(new_num_list)