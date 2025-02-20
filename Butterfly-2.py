n=int(input())
for i in range(1,n+1):
    star=i
    space=2*(n-i)
    row=("* ")*star+("  ")*space+("* ")*star
    print(row)
for i in range(n,0,-1):
    star=i
    space=2*(n-i)
    row=("* ")*star+("  ")*space+("* ")*star
    print(row)