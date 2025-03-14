list_a = [5, 4, 10, 2, 3, 2, 5, 15, 4, 4]
N=int(input())
index=[]
for i in range(len(list_a)):
    if list_a[i]==N:
        index.append(i)

print(" ".join(map(str,index)))