n=int(input())
for i in range(1,n+2):
    if(i==1):
        print("_" *(n+1))
    else:
        space=(n+1)-i
        row=("|")+(" ")*space+("/")
        print(row)