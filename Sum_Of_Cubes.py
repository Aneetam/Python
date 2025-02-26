def sum_of_cubes_m_to_n(m, n):
    # Complete this function
    sum_cube=0
    for num in range(m,n+1):
        sum_cube+=num**3
    return sum_cube
        
    


m = int(input())
n = int(input())
result=sum_of_cubes_m_to_n(m,n)
print(result)