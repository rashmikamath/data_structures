def dutch_flag(arr, pivot):
	low_boundary=0
	high_boundary = 0

	i = 0
	while i<= high_boundary:
		if arr[i]<pivot:
			swap(arr, i, low_boundary)
			low_boundary+=1
			i += 1

		if arr[i] > pivot:
			swap(arr, i, high_boundary)
			high_boundary += 1

		else:
			i +=1

def quick_sort(arr, low, high):
	random_index=random(low, high)
	pivot = dutch_flag(arr, low, high)
	quick_sort(arr, low, pivot-1)
	quick_sort(arr, pivot+1, high)