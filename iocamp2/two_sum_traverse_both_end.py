def two_sum(target, arr):
	if len(arr) == 0:
		return -1
	start = 0
	end = len(arr)-1
	while start < end:
		sum_val = arr[start]+arr[end]
		if sum_val < target:
			start += 1
		elif sum_val > target:
			end -= 1
		else:
			return (start, end)
	return -1

print(two_sum(9, [1,2,3,4,5]))