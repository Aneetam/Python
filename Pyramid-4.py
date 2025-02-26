n=int(input())
for i in range(1,n+1):
    no_stars=i
    term=str(i)+" "
    row=term*no_stars
    print(row)
for i in range(1,n):
    N=n-1
    term=str(N)+" "
    row=term*N
    print(row)
    n=n-1