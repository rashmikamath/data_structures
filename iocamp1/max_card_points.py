def max_card_points(arr, k):
	n = len(arr)
	if not k or not arr:
		return 
	if k > len(arr):
		raise ValueError()
	lsum = 0
	rsum = 0

	for i in range(0, k):
		lsum += arr[i]
	max_val = lsum
	for i in range(0, k):
		rsum += arr[n-1-i]
		lsum -= arr[k-1-i]
		max_val = max(max_val, lsum+rsum)
	return max_val
print(max_card_points([1,2,3,4,5,6,1], 4))
print(max_card_points([2,2,2], 2))
print(max_card_points([9,7,7,9,7,7,9], 7))
print(max_card_points([1,1000,1], 1))
print(max_card_points([1,79,80,1,1,1,200,1], 3))