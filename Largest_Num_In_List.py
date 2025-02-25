N=input().split()
max_num=int(N[0])
for n in N:
    # TODO: write code...
    num=int(n)
    if num>max_num:
        max_num=num
print(max_num)