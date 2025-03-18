S1=input()
S2=input()
count=0
if S1==S2:
    print(count)
else:
    for i in range(1,len(S1)+1):
    
        S1_rot=S1[-i:]+S1[:len(S1)-i]
        count+=1
        if S1_rot==S2:
            print(count)
            break
    else:
        print("No Match")