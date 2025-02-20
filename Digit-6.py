N = int(input())
rows = 2 * N - 1

for i in range(rows):
    if i == 0 or i == rows - 1 or i == N - 1:
        print("* " * N)
    elif i < N - 1:
        print("*")
    else:
        print("* " + "  " * (N - 2) + "*")