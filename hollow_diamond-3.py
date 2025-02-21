N=int(input())
for i in range(0,N):
    star=N-i
    hollow= (2*N)-(star*2)
    print("* "*star+("  ")*hollow+"* "*star)
for i in range(1,N+1):
    star=i
    hollow= (2*N)-(star*2)
    print("* "*star+("  ")*hollow+"* "*star)