M,N=map(int,input().split())

matrix=[]
for _ in range(M):
    matrix.extend(map(int,input().split()))
matrix.sort()
sorted_matrix=[]
index=0
for i in range(M):
    sorted_matrix.append(matrix[index:index+N])
    index+=N
    
for row in sorted_matrix:
    print(*row)