def get_reversed_string(string):
    # Complete this recursive function
    if len(string)<=1:
        return string
        
    return string[-1]+get_reversed_string(string[:-1])





string = input()

resultant_string = get_reversed_string(string)
print(resultant_string)