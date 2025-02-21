def replace_with_next_letters(s):
    result=[]
    for char in s:
        if 'a'<=char <='y' or 'A'<=char <="Y":
            result.append(chr(ord(char)+1))
        elif char=='z':
            result.append('a')
        elif char=='Z':
            result.append('A')
        else:
            result.append(char)
    return "".join(result)
s=input()
print(replace_with_next_letters(s))