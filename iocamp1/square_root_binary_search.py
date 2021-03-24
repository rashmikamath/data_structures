def square_root(num):
	low = 0
	high = num//2
	while low<=high:
		mid = low + (high-low)//2
		if mid*mid > num:
			high = mid-1
		elif mid*mid < num:
			if (mid+1)*(mid+1) > num:
				return mid
			low = mid + 1
		else:
			return mid
	return -1

print(square_root(36))