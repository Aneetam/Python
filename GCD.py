M=int(input())
N=int(input())
small=M if M<N else N
for i in range(small,0,-1):
    if M%i==0 and N%i==0:
        gcd=i
        break
print(gcd)