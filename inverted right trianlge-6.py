n=int(input())
for i in range(1,n+1):
    space=i-1
    star=n
    row=("  ")*space+("* ")*star
    print(row)
    n=n-1