N=int(input())
max_list=[]
for num in range(N):
    num=list(map(int,input().split()))
    num_max=max(num)
    max_list.append(num_max)
print(max_list)