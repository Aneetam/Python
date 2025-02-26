n=int(input())
for i in range(1,n+1):
    if(i==1):
        space=(n-i)
        row=(" ")*space+("*")
        print(row)
    else:
        left_spaces=n-i
        hollow_spaces=2*i-3
        row=(" ")*left_spaces+("*")+(" ")*hollow_spaces+("*")
        print(row)
for i in range(1,n):
    if(i==n-1):
        space=(n-1)
        row=(" ")*space+("*")
        print(row)
    else:
        left_spaces=i
        hollow_spaces=2*(n-i)-3
        row=(" ")*left_spaces+("*")+(" ")*hollow_spaces+("*")
        print(row)