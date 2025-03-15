def rotate_left(input_list,D):
    n=D%len(input_list)
    modfied_input_list=input_list[n:]+input_list[:n]
    return modfied_input_list


input_list=list(map(int,input().split(",")))
D=int(input())
modfied_input_list=rotate_left(input_list,D)
print(modfied_input_list)