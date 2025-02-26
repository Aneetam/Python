n=int(input())
for i in range(1,n+1):
    if(i==1):
        space=2*n-2
        row=("* ")+("  ")*space+("*")
        print(row)
    elif(i==n):
        space=n-2
        row="* "+("  ")*space+"* "+"* "+("  ")*space+("*")
        print(row)
    else:
        left=i-2
        right=i-2
        hallow=2*(n-i)
        row="* "+("  ")*left+"* "+("  ")*hallow+"* "+("  ")*right+"*"
        print(row)
for i in range(1,n+1):
    if(i==1):
        space=n-2
        row="* "+("  ")*space+"* "+"* "+("  ")*space+("*")
        print(row)
    elif(i==n):
        space=2*n-2
        row=("* ")+("  ")*space+("*")
        print(row)
    else:
        left=n-i-1
        right=n-i-1
        hallow=2*i-2
        row="* "+("  ")*left+"* "+("  ")*hallow+"* "+("  ")*right+"*"
        print(row)