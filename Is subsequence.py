full_string=input()
subsequence=input()
subseq_index=0
subsequence_length=len(subsequence)
for char in full_string:
    if char==subsequence[subseq_index]:
        subseq_index+=1
        if(subseq_index==subsequence_length):
            break
if(subseq_index==subsequence_length):
    print("Yes")
else:
    print("No")