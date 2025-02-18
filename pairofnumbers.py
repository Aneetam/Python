n=int(input())
sum=0
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i<j):
            sum=i+j
            if(sum==n):
                count+=1
print(count)




    