N=int(input())
K=int(input())
factors=[]
for i in range(1,N+1):
    if N%i==0:
        factors.append(i)
factors.sort(reverse=True)
if K<len(factors):
    print(factors[K-1])