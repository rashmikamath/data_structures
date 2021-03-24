def binary_search_duplicate(a, target):
	low = 0
	high = len(a)-1
	while low<=high:
		mid = low+(high-low)//2
		if (a[mid] > target) or (a[mid]==target and mid>0 and a[mid-1]==target):
			high = mid-1
		elif a[mid] < target:
			low = mid+1
		else:
			return mid
	return -1

print(binary_search_duplicate([1,2,2,3,4,5], 2))