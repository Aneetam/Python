S=input()
S_without_vowel=[]
Vowels=["A","E","I","O","U","a","e","i","o","u"]
for i in S:
    if i not in Vowels:
        S_without_vowel.append(i)
print("".join(S_without_vowel))