# Returns the rotated list
def rightRotate(lists, num):
	# Handle cases where num > len(lists)
	num = num % len(lists)
	
	# Will add values from n to the new list
	output_list = lists[-num:] + lists[:-num]

	return output_list


# Driver Code
rotate_num = 6
list_1 = [3, 4, 5, 6]

print(rightRotate(list_1, rotate_num))