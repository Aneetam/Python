N=int(input())
names=[input().strip() for _ in range(N)]
for name in names[::-1]:
    print(name)