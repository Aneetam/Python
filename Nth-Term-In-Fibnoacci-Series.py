def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    # Complete this function to return nth term in fibonacci series

def get_fibonacci_series(n):
    # Complete this function to return list of n terms of fibonacci series
    return [fibonacci(i) for i in range(n)]

n = int(input())
print(get_fibonacci_series(n))