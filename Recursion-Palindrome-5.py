def is_palindrome(string):
    if len(string)==0:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return is_palindrome(string[1:-1])




string = input().lower()

is_true = is_palindrome(string)

print(is_true)