names=input().split(",")
IDs=input().split(",")
student=dict(zip(names,IDs))
student_sorted=sorted(student.items())
for name,IDs in student_sorted:
    print(f"{name} {IDs}")