n=int(input())
for i in range(1,n+1):
    plus=i-1
    space=n-i
    row=("  ")*space+("+ ")*plus+("#")
    print(row)
for i in range(1,n):
    pluss=n-i-1
    space=i
    row=("  ")*space+("+ ")*pluss+("#")
    print(row)