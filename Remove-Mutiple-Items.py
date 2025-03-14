num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
N=set(map(int,input().split( )))
for num in N:
    if num in num_set:
        num_set.remove(num)
num_set_list=list(num_set)
num_set_list.sort()
print(num_set_list)