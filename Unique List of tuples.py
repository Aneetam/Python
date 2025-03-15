N=int(input())
unique_list=[]
for i in range(N):
    input_list=list(map(int,input().split()))
    input_set=set(input_list)
    if len(input_list) == len(input_set):
        unique_list.append(input_list)
print(unique_list)