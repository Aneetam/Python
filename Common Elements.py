set1=set(map(int,input().split(",")))
set2=set(map(int,input().split(",")))
common_elements=sorted(list(set1 & set2))
print(common_elements)