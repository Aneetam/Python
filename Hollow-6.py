n=int(input())
for i in range(1,n+1):
    if(i==1):
        print(". ")
    elif(i==n):
        print(". "*n)
    else:
        zero=i-2
        row=(". ")+("0 "*zero)+(". ")
        print(row)