def reverse_str(string):
    if(len(string)==0 or len(string)==1):
        return string
    else:
        return string[len(string)-1]+reverse_str(string[:len(string)-1])
        
        


string="Aneeta"
print(reverse_str(string))