n=int(input())
min_so_far=None
for _ in range(n):
    num=int(input())
    if min_so_far is None or num<min_so_far:
        min_so_far=num
    print(min_so_far)