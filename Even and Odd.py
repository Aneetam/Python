M=int(input())
N=int(input())
count_even=0
count_odd=0
for i in range(M,N+1):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(count_odd)
print(count_even)