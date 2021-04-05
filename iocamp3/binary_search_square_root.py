def square_root(x):
	low = 0
	high = x//2
	while low<=high:
		mid = low+(high-low)//2
		if square(mid) > x:
			high = mid-1
		elif square(mid)<x:
			if square(mid+1)>x:
				return mid 
			low = mid+1
		else:
			return mid
def square(x):
	return x*x

print(square_root(9))