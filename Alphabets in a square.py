N = int(input())

for i in range(N):
    for j in range(N):
        print(chr(65 + j), end=" ")  # 65 is ASCII for 'A'
    print()