def dutch_flag(arr, pivot):
	low_boundary = 0
	high_boundary = len(arr)-1
	i = 0
	while i <= high_boundary:
		if arr[i]<pivot:
			swap(arr, i, low_boundary)
			low_boundary += 1
			i += 1
		elif arr[i]>pivot:
			swap(arr, i, high_boundary)
			high_boundary -= 1
		else:
			i += 1
	return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

print(dutch_flag([1,0,4,2,4,9,4,4], 4))