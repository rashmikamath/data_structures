def find_peak(arr):
	low = 0
	high = len(arr)-1
	while low <=high:
		mid = low+(high-low)//2
		if mid > 0:
			left = arr[mid-1]
		else:
			left = float("-inf")

		if mid<len(arr)-1:
			right = arr[mid+1]
		else:
			right = float("-inf")

		if arr[mid] > right and arr[mid]<left:
			high = mid-1
		elif arr[mid]<right and arr[mid]>left:
			low = mid+1
		elif arr[mid] < right and arr[mid]<left:
			high = mid-1
		else:
			return mid
	return -1

print(find_peak([1,3,4,5,2]))