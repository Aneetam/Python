M=int(input())
N=int(input())
if M>N:
    larger=M
else:
    larger=N
while True:
    if larger%M==0 and larger%N==0:
        lcm=larger
        break
    larger+=1
print(larger)