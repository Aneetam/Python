def get_sum_of_series(X,N,term=0):
    if N==0:
        return 0
    return (X-term)+get_sum_of_series(X,N-1,term+2)




X = int(input())
N = int(input())

series_sum = get_sum_of_series(X,N)
print(series_sum)