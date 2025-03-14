n = int(input()) 

m = [] 

for i in range(n):

    c = input().split()

    if c[0]=='insert':

        i = int(c[1])

        v = int(c[2]) 

        m.insert(i,v) 

    elif c[0]=='append':

        v=int(c[1]) 

        m.append(v)

    elif c[0]=='pop':

        m.pop()

    elif c[0]=="remove":

        v=int(c[1]) 

        m.remove(v)  

    elif c[0]=="sort":

        m.sort()

    elif c[0]=="print":

        print(m)