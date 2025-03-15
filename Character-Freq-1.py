def print_char_frequency(line):
    line=line.lower()
    unique_char=set(line)
    unique_char.discard(' ')
    unique_char=sorted(unique_char)
    for char in unique_char:
        msg="{}:{}"
        print(msg.format(char,line.count(char)))




line=input()
print_char_frequency(line)