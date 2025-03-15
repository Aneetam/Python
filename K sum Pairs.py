numbers=list(map(int,input().split(",")))
K=int(input())

unique_pairs=set()
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j]==K:
            unique_pairs.add(tuple(sorted((numbers[i],numbers[j]))))
            
result=sorted(unique_pairs)
for i in result:
    print(i)