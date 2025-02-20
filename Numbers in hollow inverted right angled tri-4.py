S=int(input())
N=int(input())
num=S+(N *(N+1))//2-1
for i in range(N):
    pattern=""
    for j in range(N):
        if i==0 or j==i or j==N-1:
            pattern+=str(num)+" "
            num=num-1
        elif(j>i):
            pattern+="  "
            num=num-1
        else:
            pattern+="  "
    print(pattern.rstrip())