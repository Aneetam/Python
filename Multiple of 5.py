N=int(input())
multi=[]
for _ in range(1,N+1):
    n=int(input())
    if n%5!=0:
        multi.append(n)
    else:
        break
for item in multi:
    print(item)