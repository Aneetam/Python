S=input().split()
result=[]
for char in S[::-1]:
    result.append(char[::-1])
print(" ".join(result))