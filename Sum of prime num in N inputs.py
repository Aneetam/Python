N=int(input())
numbers=[]
prime_sum=0
for _ in range(N):
    num=int(input())
    numbers.append(num)
    prime_num=0
    
    if num>1:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            prime_sum+=num
print(prime_sum)