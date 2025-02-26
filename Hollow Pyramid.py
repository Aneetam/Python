n=int(input())
digit=""

for i in range(1,n+1):
    if(i==1):
        print(str(i))
    else:
        space=i-2
        row=(str(i)+" ")+("  ")*space+(str(i))
        print(row)
for i in range(1,n):
    if(i==n-1):
         print(str(1))
    else:
        space=2*(n-i-1)-1
        digit=n-i
        row=str(digit)+(" ")*space+str(digit)
        print(row)