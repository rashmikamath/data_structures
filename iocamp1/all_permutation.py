def find_permutation(arr, buff, buffIndex, isBuffer):
	if buffIndex == len(buff):
		print(buff[0:buffIndex])
		return 
	for i in range(0, len(arr)):
		if not isBuffer[i]:
			buff[buffIndex] = arr[i]
			isBuffer[i] = True
			find_permutation(arr, buff, buffIndex+1, isBuffer)
			isBuffer[i] = False

if __name__ == "__main__":
	arr = [1,2,3,4,5,6]
	buff = [0]*3
	isBuffer = [False]*len(arr)
	find_permutation(arr, buff, 0, isBuffer)
