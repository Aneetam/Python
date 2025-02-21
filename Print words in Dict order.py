def first_last_word(S):
    words=S.split()
    sorted_word=sorted(words,key=str.lower)
    return f"{sorted_word[0]} {sorted_word[-1]}"
    



S=input()
print(first_last_word(S))