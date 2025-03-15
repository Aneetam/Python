def convert_str_int(str_num_list):
    new_list=[]
    for item in str_num_list:
        num_list=int(item)
        new_list.append(num_list)
    return new_list

str_num_list=input().split(",")
rotate_times=int(input())
int_list=convert_str_int(str_num_list)
rotate_times=rotate_times % len(int_list)
first_part=int_list[:rotate_times]
second_part=int_list[rotate_times:]
second_part.extend(first_part)
print(second_part)