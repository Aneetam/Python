def check_unique(input_list):
    unique_elements=set(input_list)
    if len(unique_elements)==1:
        return True
    else:
        return sorted(unique_elements)
        


input_list=list(map(int,input().split()))
result=check_unique(input_list)
print(result)