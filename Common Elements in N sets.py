def find_common(set_lists):
    common_elements=set.intersection(*set_lists)
    return common_elements


N=int(input())
set_lists=[]
for i in range(N):
    elements=set(map(int,input().split()))
    set_lists.append(elements)
    
common_elements=find_common(set_lists)
print(list(sorted(common_elements)))