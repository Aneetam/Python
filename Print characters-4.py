S=input()
M=int(input())
N=int(input())
for char in S:
    for j in range(M,N+1):
        if j==ord(char):
            print(char,end=" ")