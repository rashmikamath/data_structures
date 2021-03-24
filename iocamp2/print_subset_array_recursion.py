def print_subset(arr, buff, start_index, buff_index):
	#termination case
	print(buff[:buff_index])
	if buff_index== len(buff):
		return

	if start_index==len(arr):
		return

	for i in range(start_index, len(arr)):
		buff[buff_index] = arr[i]
		print_subset(arr, buff, i+1, buff_index+1)

print_subset([1,2,3,4], [0,0,0,0], 0, 0)