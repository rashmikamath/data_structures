def combination_(arr, buffer, startIndex, bufferIndex):
	if bufferIndex == len(buffers):
		print(buffers)
		return

	if startIndex == len(arr):
		return

	for i in range(startIndex, len(arr)):
		buffers[bufferIndex] = arr[i]
		combination_(arr, buffers, i+1, bufferIndex+1)


if __name__ == "__main__":
	buffers = [0]*3
	combination_([1,2,3,4,5,6,7], buffers, 0, 0)