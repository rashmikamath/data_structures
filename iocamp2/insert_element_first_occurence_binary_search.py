def insert_at_position(arr, target):
	low = 0
	high = len(arr)-1
	while low<=high:
		mid = low + (high-low)//2
		if arr[mid] <= target:
			if mid == len(arr)-1:
				return len(arr)
			low = mid+1
		else:
			if mid==0 or arr[mid-1] <= target:
				return mid
			high = mid-1

	return -1

print(insert_at_position([1,2,4,5,6], 3))