L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]
S=input()
found=""
for char in L:
    if char==S:
        print("True")
        found=True
        break
if not found:
    print("False")
