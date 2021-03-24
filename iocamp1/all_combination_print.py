def print_combo(arr, buff, bufferIndex, startIndex):
	print(buff[0:bufferIndex])
	if bufferIndex >= len(buff):
		return

	if startIndex >= len(arr):
		return

	for i in range(startIndex, len(arr)):
		buff[bufferIndex] = arr[i]
		print_combo(arr, buff, i+1, bufferIndex+1)

if __name__ == "__main__":
	arr = [1,2,3,4]
	buff = [0]*len(arr)
	print_combo(arr, buff, 0, 0)