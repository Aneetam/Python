def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True


N=int(input())
for _ in range(N):
    num=int(input())
    if is_prime(num):
        print(num)
        break