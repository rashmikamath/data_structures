def binary_search_cyclic(a):
	low = 0
	high = len(a)-1
	right = a[len(a)-1]
	while(low <=high):
		mid = low+(high-low)//2
		if (a[mid] <= right) and (mid==0 or a[mid-1]>a[mid]):
			return mid
		elif a[mid] > right:
			low = mid+1
		else:
			high = mid-1
	return -1

print(binary_search_cyclic([4,5,6,1,2,3]))