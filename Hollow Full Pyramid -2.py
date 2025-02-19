n=int(input())
for i in range(1,n+1):
    if(i==1):
        row=""
        row+=(n-1)*(" ")+"1 "
        print(row)
    elif(i==n):
        row=""
        for j in range(0,n):
            print(1+j,end=" ")
    else:
        row=""
        left_spaces=n-i
        middle_space=2*i-4
        number=i
        row+=(" ")*left_spaces+"1 "+(" ")*middle_space+str(number)+" "
        print(row)