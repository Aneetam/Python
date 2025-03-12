def get_index(numbers_list, number,index=0):
     # Complete this recursive function
    if index>=len(numbers_list):
         return -1
    if numbers_list[index]==number:
        return index
    return get_index(numbers_list,number,index+1)
    
         
    


numbers_list = list(map(int,input().split()))
number = int(input())


number_index =get_index(numbers_list,number)

print(number_index)