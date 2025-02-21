N = int(input())
sum_of_non_primes = 0

for i in range(N):
    num = int(input())
    count = 0
    
    for j in range(2, num):
        if num % j == 0:
            count += 1
            
    if count > 0:
        sum_of_non_primes += num

print(sum_of_non_primes)