def find_peak(a):
	low = 0
	high = len(a)-1
	while low<=high:
		mid = low+(high-low)//2
		if mid > 0:
			left = a[mid-1]
		else:
			left = 0

		if mid < len(a)-1:
			right = a[mid+1]
		else:
			right = 0

		if left < a[mid] and right >a[mid]:
			low = mid+1
		elif right < a[mid] and left > a[mid]:
			high = mid-1
		elif right > a[mid] and left > a[mid]:
			high = mid-1
		else:
			return mid
	return -1
print(find_peak([7,6,5,1,2,3,4,0]))