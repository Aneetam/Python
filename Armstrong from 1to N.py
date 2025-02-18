n=int(input())

for num in range(1,n+1):
    sum_digits=0
    num_str=str(num)
    power=len(num_str)
    for digit in num_str:
        sum_digits+=int(digit) ** power
        
    if(sum_digits==num):
        print(num)