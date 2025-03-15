N=int(input())
num_list=[]
for _ in range(N):
    num_tuple=tuple(map(int,input().split()))
    num_list.append(num_tuple)
    
index_0=[t[0] for t in num_list ]
index_1=[t[1] for t in num_list ]
max_index_0=max(index_0)
min_index_0=min(index_0)
print((max_index_0,min_index_0))

max_index_1=max(index_1)
min_index_1=min(index_1)
print((max_index_1,min_index_1))