def sub_array_sum(arr, target):
	start = 0
	end = 0
	sum_val = 0
	while start < len(arr):

		if start > end:
			start = end
			sum_val = arr[start]

		if sum_val > target:
			sum_val -= arr[start]
			start += 1
		elif sum_val < target:
			if end == len(arr):
				break
			end += 1
			sum_val += arr[start]
		else:
			return(start, end)

print(sub_array_sum([5,3,1,7,6,4,2,3], 14))
