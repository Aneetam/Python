A=input().split()
B=input().split()
for i in range(1,len(A)*2,2):
    A.insert(i,B[i//2])
    
print(A)