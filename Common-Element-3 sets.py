set1=set(map(int,input().split()))
set2=set(map(int,input().split()))
set3=set(map(int,input().split()))
common_element=set1&set2&set3
print(list(common_element))