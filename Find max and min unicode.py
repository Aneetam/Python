def find_min_max_unicode(s):
    min_char=min(s)
    max_char=max(s)
    return f"{min_char} {max_char}"
    
s=input()
print(find_min_max_unicode(s))