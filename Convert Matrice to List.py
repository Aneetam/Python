m,n=input().split()
m,n=int(m),int(n)
num_list=[]
for i in range(m):
    list_a=input().split()
    row=list(map(int,list_a))
    num_list.append(row)
print(num_list)