numbers=input()
numbers=numbers.split()
result=[]
for num in numbers:
    if int(num)%3==0:
        result.append(int(num))

print(result)