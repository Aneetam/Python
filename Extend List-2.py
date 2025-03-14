N=int(input())
all_strings=[]
for _ in range(N):
    line=input()
    all_strings.extend(line.split())
    
all_strings.sort()
print(all_strings)