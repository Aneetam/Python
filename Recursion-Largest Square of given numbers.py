def get_largest_square(numbers):
    # Complete this function
    list_a=[]
    for i in numbers:
        i=int(i)
        list_a+=[i**2]
    return max(list_a)

numbers = input().split()

result =get_largest_square(numbers) # call the get_largest_square function
print(result)