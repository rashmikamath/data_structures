def min_in_cyclic_sorted_arr(a):
	low = 0
	high = len(a)-1
	right = a[len(a)-1]
	while low <= high:
		mid = low +(high-low)//2
		if a[mid]<=right and (mid==0 or a[mid-1]>a[mid]):
			return mid
		elif a[mid] > right:
			low = mid+1
		else:
			high = mid-1
	return -1
print(min_in_cyclic_sorted_arr([7,8,1,2,4,5]))