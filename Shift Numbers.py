word=input()
alpha=[]
digit=[]
for char in word:
    if char.isalpha():
        alpha.append(char)
    elif char.isdigit():
        digit.append(char)
alpha.extend(digit)
print("".join(alpha))