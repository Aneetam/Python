T=input()
last_char=T[-1]
H=0.0
if last_char=="M":
    H=float(T[0:len(T)-1])/60
    print(f"{round(H,2)}H")
elif last_char=="S":
    H=float(T[0:len(T)-1])/3600
    print(f"{round(H,2)}H")
else:
    pass