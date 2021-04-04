def binary_search(arr, target):
	low = 0
	high = len(arr)-1
	while low<=high:
		mid  = low+(high-low)//2
		if arr[mid] > target:
			if mid == 0 or arr[mid-1] <= target:
				return mid 
			else:
				high = mid-1
		elif arr[mid] <= target:
			if arr[mid] == arr[high]:
				return high+1
			else:
				low = mid+1
	return -1

print(binary_search([1,2,3,5,6], 4))
