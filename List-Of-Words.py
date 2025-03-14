S=input().split()
new_S=[]
for char in S:
    if not char.startswith('a'):
        new_S.append(char)
print(new_S)