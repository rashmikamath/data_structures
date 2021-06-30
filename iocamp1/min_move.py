def min_diff(arr):
	arr.sort()
	return min([b-a for a, b in zip(arr[:4], arr[-4:])])

print(min_diff([5,3,2,4]))
print(min_diff([1,5,0,10,14]))
print(min_diff([6,6,0,1,1,4,6]))
print(min_diff([1,5,6,14,15]))