def calculate_percentage(number):
    
    # complete this function
    if number<1000:
        result=((5/100)*number)
    else:
        result=((10/100)*number)
    return result



number = int(input())

result = calculate_percentage(number)

print(result)