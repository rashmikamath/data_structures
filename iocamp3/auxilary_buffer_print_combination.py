def print_combo(arr, k):
	if arr==None or len(arr)==None or k== None:
		return
	buff = [0]*k
	print_combo_helper(arr, buff, 0, 0)

def print_combo_helper(arr, buff, start_index, buffer_index):
	#termination case
	if buffer_index == len(buff):
		print(buff[:buffer_index])
		return

	if start_index==len(arr):
		return

	#find candidates
	for i in range(start_index, len(arr)):
		#place candidate into buffer
		buff[buffer_index] = arr[i]
		print_combo_helper(arr, buff, i+1, buffer_index+1)

print_combo([1,2,3,4,5,6,7], 3)