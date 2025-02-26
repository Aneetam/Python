S=input()
S1=""
newS=[]
for i in S:
    if(i.isupper()):
        
        newS.append("-"+i)
        
    else:
        newS.append(i)
S1="".join(newS)
print(S1.lower())