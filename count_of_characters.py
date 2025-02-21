S=input()
N=int(input())
count=0
for char in S:
    if ord(char)==N:
        count+=1
print(count)
    