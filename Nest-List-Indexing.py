num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]
# Write your code here
N=int(input())
i=0
while i <len(num_list):
    num=num_list[i]
    if N in num:
        print(i,num.index(N))
    i+=1