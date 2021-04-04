def first_occurence_of_duplicate(arr, target):
	low = 0
	high = len(arr)-1
	while low <= high:
		mid = low+(high-low)//2
		if arr[mid]>target or (arr[mid]==target and mid > 0 and arr[mid-1]==target):
			high = mid-1
		elif arr[mid]< target:
			low = mid+1
		else:
			return mid 
	return -1

print(first_occurence_of_duplicate([1,3,4,6,6,6,7], 6))