def get_digits(str1):
    digits_list=[]
    for char in str1:
        if char.isdigit():
            digits_list+=[int(char)]
    return digits_list
    
    
    
    
    
    
str1=input()
digits_list=get_digits(str1)
sum_of_digits=sum(digits_list)
print(sum_of_digits)
min_digits=min(digits_list)
print(min_digits)
max_digits=max(digits_list)
print(max_digits)