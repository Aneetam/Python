n=int(input())
digit=""
for i in range(1,n+1):
    space=n-i
    digit=str(i)+" "
    row=(" ")*space+digit*i
    print(row)
for i in range(1,n):
    space=i
    digit=str(n-1)+" "
    row=(" ")*space+digit*(n-1)
    print(row)
    n=n-1