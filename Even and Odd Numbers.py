numbers=list(map(int,input().split()))
even_numbers=sorted(num for num in numbers if num%2==0)
odd_numbers=sorted(num for num in numbers if num%2!=0)
print(even_numbers)
print(odd_numbers)Even and Odd Numbers