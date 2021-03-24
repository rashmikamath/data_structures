def find_min(arr):
	low = 0
	high = len(arr)-1
	right_pivot = arr[len(arr)-1]
	while low<=high:
		mid = low+(high-low)//2
		if (arr[mid]<=right_pivot) and (mid==0 or arr[mid-1] > arr[mid]):
			return mid
		elif arr[mid] > right_pivot:
			low = mid+1
		else:
			high = mid-1
	return -1

print(find_min([7,8,1,2,3,4,5,6]))