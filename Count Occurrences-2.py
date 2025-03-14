N=input().split()
odd_num=[]
for i in N:
    count_n=N.count(i)
    if count_n%2!=0 and int(i) not in odd_num:
        odd_num.append(int(i))
odd_num.sort()
print(odd_num)
        
    





# Read input: space-separated integers
numbers = input().split()

# Find numbers occurring an odd number of times
odd_num = sorted(set(num for num in numbers if numbers.count(num) % 2 != 0))

# Print the result
print(odd_num)