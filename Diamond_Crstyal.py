N=int(input())
for i in range(N):
    left_spaces=" "*(N-i-1)
    if i==0:
        row=left_spaces+"/"+"\\"
        print(row)
    else:
        middle_space=" "*(2*i-1)
        row=left_spaces+"/ "+middle_space+"\\"
        print(row)
for i in range(N):
    left_spaces=" "*i
    if(i==N-1):
        row=left_spaces+"\\"+"/"
        print(row)
    else:
        middle_space=" "*((N-i)*2-3)
        row=left_spaces+"\\ "+middle_space+"/"
        print(row)