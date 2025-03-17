def compute_con_sum(int_list):
    con_sum_list=[]
    for index in range(len(int_list)-1):
        con_sum=int_list[index]+int_list[index+1]
        con_sum_list.append(con_sum)
    return con_sum_list


def print_con_sum_triangle(int_list):
    while len(int_list)>1:
        con_sum_list=compute_con_sum(int_list)
        print(con_sum_list)
        int_list=con_sum_list
    


def convert_str_to_int(str_num_list):
    int_list=[]
    for item in str_num_list:
        num=int(item)
        int_list.append(num)
    return int_list
        


str_num_list=input().split(",")
int_list=convert_str_to_int(str_num_list)
print(int_list)
print_con_sum_triangle(int_list)