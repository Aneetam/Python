N=int(input())
names=[input().strip()for _ in range(N)]
result=names[:3]+names[-3:]
print(result)