def print_permutation(arr, k):
	if len(arr)==0 or arr==None or k==None:
		return
	isinBuffer = [False]*len(arr)
	buff = [0]*k
	print_permutation_helper(arr, buff, 0, isinBuffer)

def print_permutation_helper(arr, buff, buffer_index, isinBuffer):
	#termination case 
	if buffer_index == len(buff):
		print(buff[:buffer_index])
		return

	#find candidates 
	for i in range(0, len(arr)):
		if not isinBuffer[i]:
			buff[buffer_index] = arr[i]
			isinBuffer[i] = True
			print_permutation_helper(arr, buff, buffer_index+1, isinBuffer)
			isinBuffer[i] = False

print_permutation([1,2,3,4,5,6],3)