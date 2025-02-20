N = int(input())

# Find the largest factor of N that is less than N
for i in range(N - 1, 0, -1):
    if N % i == 0:
        print( i)
        break