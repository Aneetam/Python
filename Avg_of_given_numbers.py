N=input().split()
length=len(N)
sum1=0
for n in N:
    n=int(n)
    sum1+=n
print(round(sum1/length,2))