list_a = input().split(",")
list_x = []

for num in list_a:
    list_x.append(int(num)**2)
list_x.sort()
print(list_x)