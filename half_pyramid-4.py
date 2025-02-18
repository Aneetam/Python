n=int(input())
k=int(input())
K=0
for i in range(1,k+1):
    K+=i
num=n+K-1
for i in range(1,k+1):
    for j in range(i):
        print(num,end=" ")
        num=num-1
    print()