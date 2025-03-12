def calculate_power(x, y):
    # Complete this recursive function
    if y==0:
        return 1 
    return x * calculate_power(x,y-1)


a = int(input())
b = int(input())
result=calculate_power(a,b)
print(result)