n=int(input())
k=1
for i in range(n):
    for j in range(i+1):
        print(k,end=" ")
        k=k+1
    print()