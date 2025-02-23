T=input()
last_char=T[-1]
F=0.0
if last_char=="C":
    C=float(T[:-1])
    print(f"{round(float(C),2)}C")
    F=float(C)*(9/5)+32
    print(f"{round(F,2)}F")
    K=float(C)+273
    print(f"{round(K,2)}K")
elif last_char=="F":
    F=float(T[:-1])
    C=(F-32)*(5/9)
    print(f"{round(C,2)}C")
    print(f"{round(F,2)}F")
    K=C+273
    print(f"{round(K,2)}K")
elif last_char=="K":
    K=float(T[:-1])
    C=K-273
    print(f"{round(C,2)}C")
    F=C*(9/5)+32
    print(f"{round(F,2)}F")
    
    print(f"{round(K,2)}K")

    
    
