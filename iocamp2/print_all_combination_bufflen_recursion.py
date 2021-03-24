def print_combination(a, buff, start_index, buff_index):
	#terminatio case
	if buff_index==len(buff):
		print(buff)
		return
	if start_index==len(a):
		return 
	for i in range(start_index, len(a)):
		buff[buff_index] = a[i]
		print_combination(a, buff, i+1, buff_index+1)

print_combination([1,2,3,4,5,6], [0,0,0], 0, 0)