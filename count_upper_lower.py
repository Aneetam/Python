def count_of_lowercase_and_uppercase_letters(arg_1):
    # Complete this function
    count_of_uppercase=0
    count_of_lowercase=0
    for char in arg_1:
        if ord(char)>=97 and ord(char)<=122:
            count_of_lowercase+=1
        elif ord(char)>=65 and ord(char)<=90:
            count_of_uppercase+=1

    print(count_of_uppercase)
    print(count_of_lowercase)


word = input()
count_of_lowercase_and_uppercase_letters(word)
