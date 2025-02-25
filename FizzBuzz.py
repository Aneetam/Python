def fizz_buzz(number):
    # Complete this function
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)


number = int(input())
fizz_buzz(number)