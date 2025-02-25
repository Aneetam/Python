S=input().split()
first_letter=[]
for word in S:
    first_letter.append(word[0])
print(".".join(first_letter))