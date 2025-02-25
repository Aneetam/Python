S=input().split()
result=[]
for char in S:
    result.append(char[::-1])
print(" ".join(result))