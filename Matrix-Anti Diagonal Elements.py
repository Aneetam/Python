def get_diagonal_elements(num_list,m,n):
    for i in range(2*m):
        for j in range(m):
            for k in range(n):
                if j+k==i:
                    print(num_list[j][k],end=" ")
        print()

m,n=input().split()
m,n=int(m),int(n)
num_list=[]
for i in range(m):
    list_a=input().split()
    row=list(map(int,list_a))
    num_list.append(row)

get_diagonal_elements(num_list,m,n)