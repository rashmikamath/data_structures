def two_sum(arr, target):
	if len(arr)==0 or arr==None or target==None:
		return -1
	start = 0
	end = len(arr)-1
	while start <= end:
		sum_val = arr[start]+arr[end]
		if sum_val < target:
			start += 1
		elif sum_val > target:
			end -= 1
		else:
			return start,end
print(two_sum([1,2,3,4,5], 7))