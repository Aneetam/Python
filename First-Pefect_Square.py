M=int(input())
N=int(input())
for num in range(M,N+1):
    sqrt=int(num ** 0.5)
    if sqrt*sqrt==num:
        print(num)
        break
else:
    print("No Perfect Square")