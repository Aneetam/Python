def sum_of_the_digits(n):
    # Complete this recursive function
    if n<10:
        return n
        
    return (n%10)+sum_of_the_digits(n//10)


number = int(input())
# Call the sum_of_the_digits function
result=sum_of_the_digits(number)
print(result)