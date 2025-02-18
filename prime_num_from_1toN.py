n=int(input())
for number in range(2,n+1):
    num_factors=0
    for i in range(2,number):
        if(number%i==0):
            num_factors=num_factors+1
    if(num_factors==0):
        print(number)
    