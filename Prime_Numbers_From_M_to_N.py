def check_is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
    # complete this function
    
m = int(input())
n = int(input())

prime_numbers =[str(i) for i in range(m,n+1) if check_is_prime(i)]

print(" ".join(prime_numbers))