N=int(input())
for i in range(1,N+1):
   if(i==1):
       print("* " * N)
   else:
       stars=N+1-i
       print("+ " *stars)