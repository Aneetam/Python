M=int(input())
N=int(input())

for num in range(M, N + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num)
                break