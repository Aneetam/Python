N=int(input())
i=1
a=1
count=0
while a<=2:
    while count<N:
        print("* " *i)
        i=i+1
        count=count+1
    i=1
    count=0
    a=a+1