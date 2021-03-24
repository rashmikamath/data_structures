def find_peak(arr):
	low = 0
	high = len(arr)-1

	

	while low <= high:
		mid = low +(high-low)//2
		if mid > 0:
			left = arr[mid-1]
		else:
			left = 0

		if mid < len(arr)-1:
			right = arr[mid+1]
		else:
			right = 0
		if left < arr[mid] and right > arr[mid]:
			low = mid+1
		elif left > arr[mid] and right < arr[mid]:
			high = mid-1
		elif right > arr[mid] and left > arr[mid]:
			high = mid-1
		else:
			return mid 
	return -1

print(find_peak([1,3,4,5,2]))