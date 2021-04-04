def binary_search(arr, target):
	low = 0
	high = len(arr)-1
	while low<=high:
		mid = low+(high-low)//2
		if arr[mid] > target:
			high = mid-1
		elif arr[mid] < target:
			low = mid+1
		else: 
			return mid
	return -1

print(binary_search([1,2,6,7,9,10],6))
