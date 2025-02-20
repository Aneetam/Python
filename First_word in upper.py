sentence=input()
first_space_index=0
for char in sentence:
    if char==" ":
        break
    else:
        first_space_index=first_space_index+1
first_word=sentence[:first_space_index]
uppercase_first_word=first_word.upper()
new_sentence=uppercase_first_word+sentence[first_space_index:]
print(new_sentence)