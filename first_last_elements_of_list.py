N=int(input())
names=[input().strip() for _ in range(N)]
result=names[:2]+names[-2:]
print(f"[{', '.join(result)}]")