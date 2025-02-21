a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D>=0:
    r1=(-b+ D**0.5)/(2*a)
    r2=(-b- D**0.5)/(2*a)
print(round(r1,2))
print(round(r2,2))