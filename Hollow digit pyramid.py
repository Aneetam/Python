n=int(input())
for i in range(1,n+1):
    if(i==1):
        space=(n-1)
        row=str("  ")*space+str(1)
        print(row)
    else:
        left_space=n-i
        hallow_space=2*i-3
        row=("  ")*left_space+str(i)+(" ")*hallow_space+str(i)
        print(row)
for i in range(1,n):
    if(i==n-1):
        space=(n-1)
        row=str("  ")*space+str(1)
        print(row)
    else:
        left_space=i
        hallow_space=2*(n-i)-3
        num=n-i
        row=("  ")*left_space+str(num)+(" ")*hallow_space+str(num)
        print(row)