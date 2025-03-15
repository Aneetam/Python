list_a = [5, 20, 3, 7, 6, 8]
k = int(input())
list_len = len(list_a)
list_a.sort()
res = list_a[list_len - k:]
for i in range(k):
    res[i] = str(res[i])
print(" ".join(res))