N = int(input())
alpha = 65

# Upper half including middle row
for i in range(N):
    left_spaces = " " * (N - i - 1)  
    if i == 0:
        # First row has only one character 'A'
        row = left_spaces + chr(alpha)
        print(row)
        alpha += 1
    else:
        middle_spaces = " " * (2 * i - 1)  
        row = left_spaces + chr(alpha) + middle_spaces + chr(alpha + 1)
        print(row)
        alpha += 2  

# Reset alpha for lower half 
alpha -=4 

# Lower half excluding middle row 
for i in range(1,N): 
     left_spaces=" "*i 
     if(i==N-1): 
         # Last Row has only one character 'A' 
         row=left_spaces+chr(65) 
     else: 
         middle_spaces=" "*((N-i)*2-3 ) 
         row=left_spaces+chr(alpha)+middle_spaces+chr(alpha+1 ) 
     print(row ) 
     alpha-=2