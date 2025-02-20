m=11
n=20
count=0
for i in range(m+1,n):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        count=count+1
print(count)