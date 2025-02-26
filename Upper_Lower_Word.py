def get_lower_and_upper_case_letters(word):
    # Complete this function
    upper_list=[]
    lower_list=[]
    for char in word:
        if char.isupper():
            upper_list.append(char)
        else:
            lower_list.append(char)
    print("".join(upper_list))
    print("".join(lower_list))
        


word = input()
get_lower_and_upper_case_letters(word)