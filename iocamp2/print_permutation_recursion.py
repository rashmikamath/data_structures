def print_permutation(arr, buff, isBuff, buff_index):
	if buff_index==len(buff):
		print(buff)
		return
		
	for i in range(0,len(arr)):
		if not isBuff[i]:
			buff[buff_index] = arr[i]
			isBuff[i] = True
			print_permutation(arr, buff, isBuff, buff_index+1)
			isBuff[i] = False

print_permutation([1,2,3,4,5], [0,0,0], [False, False, False, False, False], 0)