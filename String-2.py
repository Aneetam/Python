S=input()
new_S=[]
new_lower=[]
new_S.append(S[0])
for i in S[1:]:
    if(i.isupper()):
        if(i!=S[0]):
            new_S.append(" "+i)
    elif(i.islower()):
        new_S.append(i)
        
S1=("".join(new_S))

print(S1)