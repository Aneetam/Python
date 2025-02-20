N = int(input())
for i in range(1, N + 1):
    left_zero = N - i
    num = 2 * i - 1
    
    print("0 " * left_zero + "1 " * num + "0 " * left_zero)