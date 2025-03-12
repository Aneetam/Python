def get_series_sum(number):
    # Complete this recursive function
    if number==1:
        return 1 
    return 1/number+get_series_sum(number-1)


number = int(input())

series_sum = get_series_sum(number)
result=round(series_sum,2)

print(result)