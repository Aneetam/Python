N=int(input())
tens=N//10
ones=N%10
if N %9==0 or tens==9 or ones==9:
    print("Lucky Number")
else:
    print("Unlucky Number")
