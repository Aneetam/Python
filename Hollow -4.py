m=int(input())
n=int(input())
for i in range(1,m+1):
    if(i==1 or i==m):
        print("* "*n)
    else:
        zero=n-2
        row=("* ")+("0 ")*zero+("* ")
        print(row)