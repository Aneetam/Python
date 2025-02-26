S=input()
S1=S[::-1]
S2=S.lower()
S3=S1.lower()
if(S2==S3):
    print("Palindrome")
else:
    print("Not a Palindrome")