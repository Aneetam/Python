students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
N=int(input())
for i in range(N):
    key,value=input().split()
    students_dict[key]=value
print(students_dict)