N=int(input())
multiple_of_2={2*i for i in range(1,N+1)}
multiple_of_3={3*i for i in range(1,N+1)}
result1=sorted(list(multiple_of_2 - multiple_of_3))
result2=sorted(list(multiple_of_2 ^ multiple_of_3))
print(result1)
print(result2)