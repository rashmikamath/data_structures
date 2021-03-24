def move_zero_end(arr):
	boundary = len(arr)-1
	for i in range(len(arr)-1, -1, -1):
		if arr[i] == 0:
			swap(arr, i, boundary)
			boundary -= 1
	return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr

print(move_zero_end([0,1,0,2,0,3,0,0,4]))